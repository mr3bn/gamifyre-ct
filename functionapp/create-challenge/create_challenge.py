"""
Azure function module to create a new document in the "Challenges" collection.
"""

import json
import os

import azure.functions as func
    
# from __app__.shared.entities import Person
from __app__.shared.mongo_wrapper import get_client, insert_one
from __app__.shared.constants import mongo as mongo_constants
from __app__.shared.constants import env as env_constants

def main(req: func.HttpRequest):

    challenge = req.get_json()

    client = get_client(os.environ[env_constants.MONGO_CONNECTION_STRING])

    insert_one(client, mongo_constants.GAMIFYRE_DB, mongo_constants.collections.CHALLENGE, challenge)

    return func.HttpResponse(status_code=200)