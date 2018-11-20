import datetime

from pymongo import MongoClient
from general.utility import get_sequence_value as custom_id, reset_sequence_value
import pprint


def new_incident(incident):
    client = MongoClient('localhost', 27017)
    db = client['Testing']
    db.authenticate('testing_admin', 'pwd4db')
    collection = db.incident
    start_date = datetime.datetime.strptime('%s 00:00:00' % incident.start_date, '%Y-%m-%d %H:%M:%S')
    due_date = datetime.datetime.strptime('%s 00:00:00' % incident.due_date, '%Y-%m-%d %H:%M:%S')
    document = {'custom_id': custom_id('tid'),
                'status': incident.status,
                'title': incident.title,
                'created_by': incident.created_by,
                'description': incident.description,
                'start_date': {'date': start_date,
                               'str_date': str(start_date.date()),
                               'ww': start_date.isocalendar()[1],
                               'year': start_date.year},
                'close_date': {'date': incident.close_date,
                               'ww': '',
                               'year': ''},
                'due_date': {'date': due_date,
                             'str_date': str(due_date.date()),
                             'ww': due_date.isocalendar()[1],
                             'year': due_date.year},
                'comments': [],
                'tags': incident.tags,
                'last_modified': datetime.datetime.utcnow(),
                'activity': [{
                    'who': incident.created_by,
                    'action': 'created',
                    'timestamp': datetime.datetime.utcnow()
                }]}
    collection.insert_one(document)
    pprint.pprint(document)


def get_incidents():
    client = MongoClient('localhost', 27017)
    db = client['Testing']
    db.authenticate('testing_admin', 'pwd4db')
    collection = db.incident.aggregate([
        {
            '$group': {
                '_id': '$status',
                'items': {
                    '$push': '$$ROOT'
                }
            }
        }, {
            '$project': {
                '_id': 1,
                'items': {
                    'custom_id': 1,
                    'status': 1,
                    'title': 1,
                    'created_by': 1,
                    'due_date': {
                        'ww': 1,
                        'str_date': 1,
                        'year': 1
                    },
                    'close_date': {
                        'ww': 1,
                        'str_date': 1,
                        'year': 1
                    },
                    'tags': 1,
                    'description': 1,
                    'comments': {
                        'ww': 1,
                        'str_date': 1,
                        'year': 1
                    },
                    'start_date': {
                        'ww': 1,
                        'str_date': 1,
                        'year': 1
                    },
                    'activity': {
                        'action': 1
                    }
                }
            }
        }
    ])
    group = {}
    for item in collection:
        group.update({item['_id']: item['items']})
    return group
