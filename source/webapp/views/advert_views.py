from urllib.parse import urlencode
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Advert, Comment
from webapp.forms import CommentForm, AdvertForm, SimpleSearchForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class IndexView(ListView):
    template_name = 'adverts/index.html'
    context_object_name = 'adverts'
    model = Advert
    paginate_by = 5
    ordering = ['-published']

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.search_form.is_valid():
            return self.search_form.cleaned_data['search']
        return None

    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(title__icontains=self.search_value) |
                                       Q(description__icontains=self.search_value))
            return queryset
        return Advert.objects.filter(advert_status='published')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context


class AdvertView(LoginRequiredMixin, DetailView):
    template_name = 'adverts/detail_advert.html'

    def get(self, request, pk):
        advert = get_object_or_404(Advert, pk=pk)
        comments = Comment.objects.filter(advert=advert)
        form = CommentForm()

        context = {'advert': advert, 'comments': comments, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        advert = get_object_or_404(Advert, pk=pk)
        comments = Comment.objects.filter(advert=advert)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.advert = advert
            comment.author = request.user
            comment.save()
            return render(request, self.template_name, {'advert': advert, 'comments': comments, 'form': CommentForm()})

        return render(request, self.template_name, {'advert': advert, 'comments': comments, 'form': form})


class AdvertCreateView(LoginRequiredMixin, CreateView):
    template_name = 'adverts/add_advert.html'
    model = Advert
    form_class = AdvertForm

    def form_valid(self, form):
        self.advert = form.save(commit=False)
        self.advert.author = self.request.user
        self.advert.save()
        return redirect('webapp:advert_view', pk=self.advert.pk)


class AdvertUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'adverts/update_advert.html'
    model = Advert
    form_class = AdvertForm
    permission_required = 'webapp.change_advert'

    def has_permission(self):
        if self.get_object().status != 'canceled':
            return super().has_permission() or self.request.user == self.get_object().author
        else:
            return False

    def form_valid(self, form):
        advert = form.save(commit=False)
        advert.advert_status = 'moderation'
        advert.save()
        return redirect('webapp:advert_view', pk=advert.pk)


class AdvertDeleteView(PermissionRequiredMixin, DeleteView):
    model = Advert
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_advert'

    def get(self, request, *args, **kwargs):
        advert = get_object_or_404(self.model, pk=kwargs['pk'])
        advert.advert_status = 'deleted'
        advert.save()
        return HttpResponseRedirect(self.success_url)

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author