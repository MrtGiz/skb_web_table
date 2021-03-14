from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import render

from .forms import ApplicationForm
from .models import Application


class ApplicationListView(ListView):
    template_name = 'application/index.html'
    model = Application
    context_object_name = 'applications'


class ApplicationCreateView(CreateView):
    template_name = 'application/createapp.html'
    form_class = ApplicationForm
    success_url = '/'


class ApplicationUpdateView(UpdateView):
    template_name = 'application/updateapp.html'
    model = Application
    form_class = ApplicationForm
    success_url = '/'


class ApplicationDeleteView(DeleteView):
    template_name = 'application/deleteapp.html'
    model = Application
    success_url = '/'
