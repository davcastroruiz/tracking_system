from django.shortcuts import render


# Create your views here.
def panel(request):
    return render(request, 'tracking/panel.html')


'''
{_id: xxxx,
status: 'Open',
title: 'Dummy Title',
created_by: ''
start_date: '',
close_date: '',
due_date: '',
comments: [{12:33 AM 11/19/2018
	who:'', 
	timestamp: '',
	comment: ''}]
tags: []}
'''
