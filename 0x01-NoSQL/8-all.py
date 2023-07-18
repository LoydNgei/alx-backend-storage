#!/usr/bin/env python3
""" A Python function that lists all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    """Return empty list if no document in collection"""
    if mongo_collection is None:
        return []

    results = mongo_collection.find()
    return [doc for doc in results]
