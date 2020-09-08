import pymongo

class MongoManager:
     __instance = None
     @staticmethod 
     def getInstance():
         if MongoManager.__instance == None:
             MongoManager(self._connection_str)
         return MongoManager.__instance
     def __init__(self, connection_str):
        if MongoManager.__instance is None:
            self._connection_str = connection_str
            MongoManager.__instance = pymongo.MongoClient(connection_str)

def get_client(mongo_str):
    return MongoManager(mongo_str).getInstance()

def insert_one(client, db, collection, document):
    coll = client[db][collection]
    coll.insert_one(document)