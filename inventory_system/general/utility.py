from pymongo import MongoClient, DESCENDING, ASCENDING
from django.conf import settings
from general.models import Messages


def get_keys(db, collection, query={}):
    client = MongoClient(settings.DATABASE_HOST, 27017)
    db = client[db]
    db.authenticate('read_user', 'read4db')
    doc = db[collection].find_one(query)
    keys = []
    for key in doc:
        if key != '_id':
            keys.append(key)
    return keys


def custom_message(message, tag):
    # 1.- success, 2.-info, 3.- warning 4.- danger
    msg = Messages()
    if tag == 0:
        msg.tag = "alert alert-success"
    elif tag == 1:
        msg.tag = "alert alert-info"
    elif tag == 2:
        msg.tag = "alert alert-warning"
    else:
        msg.tag = "alert alert-danger"

    msg.message = message

    return msg


def dictionary_try(dic, key):
    try:
        value = dic[key]
    except:
        value = ''
    return value
