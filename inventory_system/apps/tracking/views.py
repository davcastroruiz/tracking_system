from django.shortcuts import render, redirect
from apps.tracking.models import Incident
from .utility import new_incident, get_incidents


# Create your views here.
def panel(request):
    context = {
        'incidents': get_incidents(),
    }
    return render(request, 'tracking/panel.html', context)


def create_incident(request):
    if request.method:
        incident = Incident
        incident.created_by = str(request.user)
        incident.tags = list(filter(None, request.POST['tags'].split(',')))
        incident.title = request.POST['title']
        incident.status = request.POST['status']
        incident.start_date = request.POST['start-date']
        incident.due_date = request.POST['due-date']
        incident.description = str(request.POST['description']).replace('\n', '<br>').replace('\r', '&nbsp;')
        new_incident(incident)
    return redirect('tracking:panel_dashboard')


'''
{custom_id: get_sequence_value('tid'),
status: 'Open',
title: 'Dummy Title',
created_by: 'request'
start_date: 'request',
close_date: '',
due_date: 'request',
comments: [{12:33 AM 11/19/2018
	who:'', 
	timestamp: '',
	comment: ''}]
tags: [],
activity: [{
    who:'',
    timestamp:''
    action: ''}]}
'''
