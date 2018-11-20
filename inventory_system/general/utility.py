from pymongo import MongoClient, DESCENDING, ASCENDING
from general.models import Messages


def get_keys(db, collection, query=None):
    if query is None:
        query = {}
    client = MongoClient('localhost', 27017)
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
    except Exception as e:
        value = ''
    return value


def get_sequence_value(sequence_name):
    '''In order of use sequence value as auto increment ID
    you need to create counters collections in the database that you want to use
    example:
    use Testing
    db.counters.insert({_id:"tid",sequence_value:0})
    once you insert this document you can use sequence value function
    if you need to reset the counter just update "tid" to 0
    db.scores.findOneAndUpdate({ _id: "tid"},
   { $set: { sequence_value : 0 } })
    '''
    client = MongoClient('localhost', 27017)
    db = client['Testing']
    db.authenticate('testing_admin', 'pwd4db')
    sequence_document = db.counters.find_one_and_update({'_id': sequence_name},
                                                        {"$inc": {'sequence_value': 1}},
                                                        upsert=True,
                                                        )
    return int(sequence_document['sequence_value'])


def reset_sequence_value(sequence_name):
    client = MongoClient('localhost', 27017)
    db = client['Testing']
    db.authenticate('testing_admin', 'pwd4db')
    db.counters.find_one_and_update({'_id': sequence_name},
                                    {"$set": {'sequence_value': 1}},
                                    upsert=True,
                                    )

# reset_sequence_value('tid')
