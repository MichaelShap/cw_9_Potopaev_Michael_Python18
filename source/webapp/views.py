from django.shortcuts import get_object_or_404, reverse, redirect, render

from accounts.models import User
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def index(request):
    return render(request, 'index.html')