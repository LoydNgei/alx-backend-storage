#!/usr/bin/env python3
""" a Python function that changes all topics of a school document based on the name"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Change school topics"""
    results = mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    
    return results
