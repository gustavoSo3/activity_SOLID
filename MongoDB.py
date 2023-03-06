from pymongo import MongoClient
from unittest import result

client = pymongo.MongoClient("mongodb+srv://admin:root@cluster0.muthfez.mongodb.net/?retryWrites=true&w=majority")
# db = client['testStore']
db = client.test
collection = db['productos']

# collection.insert_one({"_id": 1,
#                       "name": "Gansito",
#                       "precio": 20})

results = collection.find()
for r in result:
    print(r)
