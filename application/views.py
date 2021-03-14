from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django_filters.views import FilterMixin

from .forms import ApplicationForm
from .models import Application
from .filters import AppFilter
from .utils.export import Export


class ApplicationListView(ListView, FilterMixin):
    template_name = 'application/index.html'
    model = Application
    filterset_class = AppFilter
    context_object_name = 'applications'

    def get_queryset(self):
        orderby = self.request.GET.get('orderby', 'date')
        new_queryset = Application.objects.all().order_by(orderby)
        return new_queryset

    def get(self, request, *args, **kwargs):
        self.filterset = self.get_filterset(self.get_filterset_class())
        self.object_list = self.filterset.qs
        context = self.get_context_data(filter=self.filterset, object_list=self.object_list)
        return self.render_to_response(context)


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


def export_to_csv(request):
    response = Export().export_to_csv()
    return response


def export_to_xls(request):
    response = Export().export_to_excel()
    return response
