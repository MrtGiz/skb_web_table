from django.urls import path
from .views import ApplicationListView, ApplicationCreateView, ApplicationUpdateView, ApplicationDeleteView, \
    export_to_csv, export_to_xls


app_name = 'app'

urlpatterns = [
    path('', ApplicationListView.as_view(), name='index'),
    path('create/', ApplicationCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ApplicationUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ApplicationDeleteView.as_view(), name='delete'),
    path('export/csv/', export_to_csv, name='export_csv'),
    path('export/xls/', export_to_xls, name='export_xls'),

]
