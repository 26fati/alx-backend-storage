#!/usr/bin/env python3
'''
    a function that returns all students sorted by average score.
'''
from bson.son import SON


def top_students(mongo_collection):
    ' a function that returns all students sorted by average score'
    results = mongo_collection.aggregate([
        {"$unwind": "$topics"},
        {"$group": {
            "_id": {
                "_id": "$_id",
                "name": "$name"
            },
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$project": {
            "_id": "$_id._id",
            "name": "$_id.name",
            "averageScore": 1
        }},
        {"$sort": SON([("averageScore", -1)])}
    ])
    return list(results)
