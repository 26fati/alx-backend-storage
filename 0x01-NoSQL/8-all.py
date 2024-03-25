#!/usr/bin/env python3
'''
    a function that lists all documents in a collection.
'''


def list_all(mongo_collection):
    ' a function that lists all documents in a collection.'
    if mongo_collection is None:
        return []
    return [document for document in mongo_collection.find()]
