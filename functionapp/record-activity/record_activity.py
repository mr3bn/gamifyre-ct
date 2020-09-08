"""
Azure function module to log a person's completion of a challenge
"""

import logging
import os 

import azure.functions as func
from bson.objectid import ObjectId

from __app__.shared.constants import env as env_constants
from __app__.shared.constants import mongo as mongo_constants
from __app__.shared.mongo_wrapper import get_client

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    person_id, activity_id = process_request(req)

    if not person_id:
        return func.HttpResponse(f'Bad request. Missing required query parameter personId', status_code=400)
    if not activity_id:
        return func.HttpResponse(f'Bad request. Missing required query parameter activityId', status_code=400)

    person_object_id = ObjectId(person_id)
    activity_object_id = ObjectId(activity_id)

    client = get_client(os.environ[env_constants.MONGO_CONNECTION_STRING])

    append_activity_to_person(client, person_object_id, activity_object_id)

    return func.HttpResponse(status_code=200)

def process_request(req: func.HttpRequest):
    """Pulls and returns required query paramters named personId and activityId from an incoming func.HttpRequest"""

    person_id = req.params.get('personId')
    activity_id = req.params.get('activityId')

    return person_id, activity_id

def append_activity_to_person(client, person_object_id, activity_object_id):
    """Updates one 'person' document by appending an activityId reference to the <person>.completedActivities array"""

    person = client.gamifyre.person.find_one({'_id':person_object_id})

    if not person.get('completedActivities'):
        return client.gamifyre.person.update_one({'_id':person_object_id}, {'$set': {'completedActivities': [activity_object_id]}})

    return client.gamifyre.person.update_one({'_id':person_object_id}, {'$push': {'completedActivities': activity_object_id}})