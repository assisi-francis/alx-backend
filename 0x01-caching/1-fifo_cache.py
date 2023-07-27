#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from BaseCaching and is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and implements FIFO caching
    """

    def __init__(self):
        """ Initialize the FIFO cache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache (FIFO algorithm)
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.queue:
                    # Get the key of the first item put in the cache (FIFO)
                    discarded_key = self.queue.pop(0)
                    del self.cache_data[discarded_key]
                    print("DISCARD:", discarded_key)

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
