"""Azure function module for the /activities/get_activities function

Returns:
    HttpResponse 
    code
"""

import logging
import os

import azure.functions as func
from bson.objectid import ObjectId

from __app__.shared.mongo_wrapper import get_client
from __app__.shared.constants import env as env_constants


def main(req: func.HttpRequest) -> func.HttpResponse:

    # Get the challengeId out of the URL
    challenge_id = req.route_params.get('challengeId')

    # Get the special opbject ID type
    challenge_object_id = ObjectId(challenge_id)

    # Set up the mongo client
    client = get_client(os.environ[env_constants.MONGO_CONNECTION_STRING])

    # Get all Activites that have a challenge_id = challengeId and add to a JSON 
    # object
    activities = []
    for record in client.gamifyre.activity.find( {"challenge_id":challenge_object_id} ):
        
        activities = activities + record


    return func.HttpResponse(body=str(activities), status_code=200)  