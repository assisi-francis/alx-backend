#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits from BaseCaching and is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching and implements LIFO caching
    """

    def __init__(self):
        """ Initialize the LIFO cache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache (LIFO algorithm)
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.queue:
                    # Get the key of the last item put in the cache (LIFO)
                    discarded_key = self.queue.pop()
                    del self.cache_data[discarded_key]
                    print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
