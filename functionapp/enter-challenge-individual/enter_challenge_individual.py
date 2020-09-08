"""
Azure function module to enter an individual person into a challenge.
"""

import logging
import os

import azure.functions as func
from bson.dbref import DBRef
from bson.objectid import ObjectId

from __app__.shared.constants import env as env_constants
from __app__.shared.constants import mongo as mongo_constants
from __app__.shared.mongo_wrapper import get_client

def main(req: func.HttpRequest) -> func.HttpResponse:

    person_id, challenge_id = process_request(req)

    if not person_id:
        return func.HttpResponse(f'Bad request. Missing required query parameter personId', status_code=400)
    if not challenge_id: 
        return func.HttpResponse(f'Bad request. Missing required query parameter challengeId', status_code=400)

    logging.info(str((person_id, challenge_id)))

    person_object_id = ObjectId(person_id)
    challenge_object_id = ObjectId(challenge_id)

    client = get_client(os.environ[env_constants.MONGO_CONNECTION_STRING])
    
    append_challenge_to_person(client, person_object_id, challenge_object_id)
    append_person_to_challenge(client, person_object_id, challenge_object_id)

    return func.HttpResponse(status_code=200)

def process_request(req: func.HttpRequest):
    """Pulls and returns required query parameters from an incoming func.HttpRequest"""

    person_id = req.params.get('personId')
    challenge_id = req.params.get('challengeId')

    return person_id, challenge_id

def append_challenge_to_person(client, person_object_id, challenge_object_id):
    """Updates one 'person' document by appending a challenge_id reference to the <person>.challenges array."""

    person = client.gamifyre.person.find_one({'_id':person_object_id})
    
    if not person.get('challenges'):
        # if null or missing challenge property append new array with specified challenge
        return client.gamifyre.person.update_one({'_id':person_object_id}, {'$set': {'challenges': [challenge_object_id]}})
    
    # if challenge property exists, append challenge to it
    return client.gamifyre.person.update_one({'_id':person_object_id}, {'$push': {'challenges': challenge_object_id}})

def append_person_to_challenge(client, person_object_id, challenge_object_id):
    """Updates one 'challenge' document by appending a person_id reference to the <challenge>.enrolledIndividuals array"""
    
    challenge = client.gamifyre.challenge.find_one({'_id':challenge_object_id})

    if not challenge.get('enrolledIndividuals'):
        return client.gamifyre.challenge.update_one({'_id':challenge_object_id}, {'$set': {'enrolledIndividuals': [person_object_id]}})

    return client.gamifyre.challenge.update_one({'_id':challenge_object_id}, {'$push':{'enrolledIndividuals': challenge_object_id}})