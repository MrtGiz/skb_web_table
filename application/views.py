from django.views.generic import CreateView, ListView
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
    success_url = 'application/index.html'


