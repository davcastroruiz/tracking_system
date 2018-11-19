from django.urls import path, re_path
from . import views

app_name = 'tracking'

urlpatterns = [
    path('', views.panel, name='example')
]