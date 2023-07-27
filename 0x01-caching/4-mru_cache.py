#!/usr/bin/env python3
"""
Create a class MRUCache that inherits from BaseCaching and is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and implements MRU caching
    """

    def __init__(self):
        """ Initialize the MRU cache
        """
        super().__init__()
        self.queue = []  # To keep track of access order (most recently used at the end)

    def put(self, key, item):
        """ Add an item in the cache (MRU algorithm)
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get the most recently used key (last element in the queue)
                discarded_key = self.queue.pop()
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            self.cache_data[key] = item
            self.queue.insert(0, key)  # Insert the key at the front to indicate most recently used

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            # Move the accessed key to the front of the queue (most recently used)
            self.queue.remove(key)
            self.queue.insert(0, key)
            return self.cache_data[key]
        return None
