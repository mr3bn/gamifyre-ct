"""Azure function module for the /challenges/get_challenge function

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

    challenge_id = req.route_params.get('challengeId')

    challenge_object_id = ObjectId(challenge_id)

    client = get_client(os.environ[env_constants.MONGO_CONNECTION_STRING])

    challenge = client.gamifyre.challenge.find_one({"_id":challenge_object_id})

    return func.HttpResponse(body=str(challenge), status_code=200)    
    
