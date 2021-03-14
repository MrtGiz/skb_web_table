from django.urls import path
from .views import ApplicationListView, ApplicationCreateView, ApplicationUpdateView, ApplicationDeleteView, \
    export_to_csv, export_to_xls, count_by_month, last_app_for_client


app_name = 'app'

urlpatterns = [
    path('', ApplicationListView.as_view(), name='index'),
    path('create/', ApplicationCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ApplicationUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ApplicationDeleteView.as_view(), name='delete'),
    path('export/csv/', export_to_csv, name='export_csv'),
    path('export/xls/', export_to_xls, name='export_xls'),
    path('query/count/', count_by_month, name='count_by_month'),
    path('query/last_app/', last_app_for_client, name='last_app'),
]
