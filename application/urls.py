from django.urls import path
from .views import ApplicationListView, ApplicationCreateView, ApplicationUpdateView, ApplicationDeleteView


app_name = 'app'

urlpatterns = [
    path('', ApplicationListView.as_view(), name='index'),
    path('create/', ApplicationCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ApplicationUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ApplicationDeleteView.as_view(), name='delete'),
]