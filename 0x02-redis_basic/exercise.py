#!/usr/bin/env python3
"""This script is used to execute some instructions """
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """This class is used to create a cache"""

    def __init__(self):
        """Constructor to store an instace of Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """This method is used to generate a random key and store"""
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key
