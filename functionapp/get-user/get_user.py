"""Azure function module for the /user/{username} function
"""

import logging
import os

import azure.functions as func

from __app__.shared.mongo_wrapper import get_client
from __app__.shared.constants import env as env_constants
    
def main(req: func.HttpRequest) -> func.HttpResponse:
    username = req.route_params.get('username')
    
    client = get_client(os.environ[env_constants.MONGO_CONNECTION_STRING])

    user = client.gamifyre.person.find_one({"uname":username})

    return func.HttpResponse(body=str(user), status_code=200)