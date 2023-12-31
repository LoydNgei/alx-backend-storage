#!/usr/bin/env python3
""" a Python function that returns the list of school having a specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Return lst of school"""
    results = mongo_collection.find({"topics": topic})
    return results
