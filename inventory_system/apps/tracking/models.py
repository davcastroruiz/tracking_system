from django.db import models


# Create your models here.
class Incident:
    def __init__(self):
        self.status = ''
        self.title = ''
        self.created_by = ''
        self.start_date = ''
        self.close_date = ''
        self.due_date = ''
        self.tags = []
        self.comments = []
        self.activity = []
        self.description = ''

    status = ''
    title = ''
    created_by = ''
    start_date = ''
    close_date = ''
    due_date = ''
    tags = []
    comments = []
    activity = []
    description = ''
