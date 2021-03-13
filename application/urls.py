from django.urls import path
from .views import ApplicationListView, ApplicationCreateView


app_name = 'app'

urlpatterns = [
    path('', ApplicationListView.as_view(), name='index'),
    path('create/', ApplicationCreateView.as_view(), name='create'),
]