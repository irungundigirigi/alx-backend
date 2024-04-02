#!/usr/bin/env python3

"""
module: 1-fifo_cache.py
"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
    Initialize the class with parents init
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Cache a key-value pair in a FIFO cache
        """
        if None in (key, item):
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                last_in = list(self.cache_data.keys())[-1]
                print(f'DISCARD: {last_in}')
                del self.cache_data[last_in]
            if key in self.cache_data.keys():
                del self.cache_data[key]
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key, or None
        """
        if key is None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
