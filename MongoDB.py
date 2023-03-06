from pymongo import MongoClient
import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:root@cluster0.muthfez.mongodb.net/?retryWrites=true&w=majority")
db = client.test



# print(client)