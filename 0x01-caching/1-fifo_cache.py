#!/usr/bin/env python3

"""
module: 1-fifo_cache.py
compactible with python >3.7 where dict keeps order of insertion
"""
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
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
                first_in = next(iter(self.cache_data))
                print(f'DISCARD: {first_in}')
                del self.cache_data[first_in]
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key, or None
        """
        if key is None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
