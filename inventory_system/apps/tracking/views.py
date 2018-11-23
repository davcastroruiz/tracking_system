from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from apps.tracking.models import Incident
from .utility import new_incident, get_incidents, set_status_incident, datetime, set_comment_incident, get_comments


# Create your views here.
def panel(request):
    today = datetime.datetime.utcnow()
    context = {
        'ww': today.isocalendar()[1],
        'year': today.year,
        'incidents': get_incidents(),
    }
    return render(request, 'tracking/panel.html', context)


def create_incident(request):
    if request.method == "POST":
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


@csrf_exempt
def new_comment(request):
    comment = request.POST['new_comment']
    custom_id = int(request.POST['custom_id'])

    try:
        set_comment_incident(custom_id, comment, str(request.user))

        data = {
            'success': True
        }
    except Exception as e:
        data = {
            'exception': e
        }
    return JsonResponse(data)


@csrf_exempt
def update_incident_status(request):
    status = request.POST['status']
    custom_id = int(request.POST['custom_id'])

    try:
        set_status_incident(custom_id, status, str(request.user))
        data = {
            'success': True
        }
    except Exception as e:
        data = {
            'exception': e
        }
    return JsonResponse(data)


def get_comments_incident(request):
    custom_id = int(request.GET['custom_id'])
    try:
        data = {
            'success': True,
            'comments': get_comments(custom_id)
        }
    except Exception as e:
        data = {
            'exception': e
        }
    return JsonResponse(data)


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
