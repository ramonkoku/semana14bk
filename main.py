from pymongo import MongoClient

mongo_uri = "mongodb+srv://koku_api_py:<db_password>@cluster0.qdcmbwk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo_client = MongoClient(mongo_uri) 

