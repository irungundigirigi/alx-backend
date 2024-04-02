#!/usr/bin/env python3
""" Basic caching module
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):

    """
    Defines a class for caching data  in key-value pairs
    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """

    def __init__(self):
         """
        Initialize class using parents __init__ method
        """
        super().__init__()

    def put(self, key, item):
        """
        Store a key-value pair
        Args:
            Key
            Item
        """
        if None in (key, item):
            pass
        else:
            self.cache_data[key] = item


    def get(self, key):
        """
        Return value linked to key.
        If key is None or doesn't exist, return None
        """
        if None in (key, self.cache_data.get(key)):
            pass
        else:
            return self.cache_data.get(key)





