"""
Azure function module to create a new document in the "Activity" collection.
"""

import json
import os

import logging

import azure.functions as func

from __app__.shared.constants import mongo as mongo_constants
from __app__.shared.constants import env as env_constants
from __app__.shared.mongo_wrapper import get_client, insert_one

def main(req: func.HttpRequest):

    # SAMPLE req.get_json()
    # {
    #     "challenge_id": "5f56eca4616f41ee0202134d",
    #     "name": "Daily Reading",
    #     "record_rules": [
    #         {
    #             "name": "Read for 30 Minutes",
    #             "type": "Type 1",
    #             "required": true
    #         }
    #     ],
    #     "repeat_rules": {
    #         "repeats_allowed": true,
    #         "repeat_frequency": "daily"
    #     },
    #     "reward_rules": {
    #         "frequency_mutiplier": "5"
    #     },
    #     "completion_criteria": {
    #         "team_completion": false
    #     }
    # }
    activity = req.get_json()

    client = get_client(os.environ[env_constants.MONGO_CONNECTION_STRING])

    insert_one(client, mongo_constants.GAMIFYRE_DB, mongo_constants.collections.ACTIVITY, activity)

    return func.HttpResponse(status_code=200)
