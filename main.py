from pymongo import MongoClient
from dotenv import dotenv_values

mongo_uri = "mongodb+srv://koku_api_py:Ko15311015ku@cluster0.qdcmbwk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo_client = MongoClient(mongo_uri) 

database = mongo_client['database_test']
test_collection = database ['test_collection']

person = {"name": "lucca de enzo", "age": 12}
test_collection.insert_one(person)

config = dotenv_values('.env')
mongo_uri = config ['URI_MONGO_ATLAS']

mongo_client = MongoClient(mongo_uri)