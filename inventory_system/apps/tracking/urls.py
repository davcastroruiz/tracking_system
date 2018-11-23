from django.urls import path, re_path
from . import views

app_name = 'tracking'

urlpatterns = [
    path('', views.panel, name='panel_dashboard'),
    path('ajax/update_status', views.update_incident_status, name='update_status'),
    path('ajax/new_comment', views.new_comment, name='new_comment'),
    path('ajax/get_comments_incident', views.get_comments_incident, name='get_comments_incident'),
    path('post/incident', views.create_incident, name='create_incident')
]
