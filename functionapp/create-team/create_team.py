"""
Azure function module to create a new document in the "Teams" collection.
"""

import json
import os

import azure.functions as func
    
from __app__.shared.constants import mongo as mongo_constants
from __app__.shared.constants import env as env_constants
from __app__.shared.mongo_wrapper import get_client, insert_one

def main(req: func.HttpRequest):

    team = req.get_json()

    if 'members' not in team.keys():
        team["members"] = [team["owner_id"]]

    if 'challeneges' not in team.keys():
        team["challenges"] = []

    if 'activities' not in team.keys():
        team["activities"] = []


    client = get_client(os.environ[env_constants.MONGO_CONNECTION_STRING])

    insert_one(client, mongo_constants.GAMIFYRE_DB, mongo_constants.collections.TEAM, team)

    return func.HttpResponse(status_code=200)