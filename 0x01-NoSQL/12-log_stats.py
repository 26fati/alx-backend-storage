#!/usr/bin/env python3
'''
    a Python script that provides some
    stats about Nginx logs stored in MongoDB.
'''
from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.logs
nginx = db.nginx

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
logs = nginx.count_documents({})
print("{} logs".format(logs))
print("Methods:")
for method in methods:
    number = nginx.count_documents({"method": method})
    print("\tmethod {}: {}".format(method, number))
number_status = nginx.count_documents(
    {"method": 'GET', "path": {"$regex": "^/status"}})
print("{} status check".format(number_status))
