#!/usr/bin/env python3
'''
    Improve 12-log_stats.py by adding
    the top 10 of the most present IPs
    in the collection nginx of the
    database logs
'''
from pymongo import MongoClient
from bson.son import SON


if __name__ == "__main__":
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

    results = nginx.aggregate([
            {"$group": {
                "_id": "$ip",
                "sum": {"$sum": 1}
            }},
            {"$sort": SON([("sum", -1)])}
        ])
    print("IPS:")
    lst = list(results)
    for i in range(10):
        print("\t{}: {}".format(lst[i].get("_id"), lst[i].get("sum")))
