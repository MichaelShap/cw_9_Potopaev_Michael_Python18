from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from webapp.models import Comment
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

class CommentDeleteView(PermissionRequiredMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_comment'

    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(self.model, pk=kwargs['pk'])
        comment.delete()
        return HttpResponseRedirect(self.success_url)

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author