from bson.objectid import ObjectId
from pymongo import MongoClient


def get_mongo_db():
    client = MongoClient("mongodb://localhost")
    db = client.hw_10
    return db
