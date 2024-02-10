from datetime import timezone

from django.shortcuts import render, get_object_or_404, reverse, redirect
from webapp.models import Advert, Category, Comment
from webapp.forms import CommentForm, AdvertForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class IndexView(ListView):
    template_name = 'adverts/index.html'
    context_object_name = 'adverts'
    model = Advert
    paginate_by = 5
    ordering = ['-published']

    def get_queryset(self):
        return Advert.objects.filter(advert_status='published')

