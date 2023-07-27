#!/usr/bin/env python3
"""
Create a class LRUCache that inherits from BaseCaching and is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and implements LRU caching
    """

    def __init__(self):
        """ Initialize the LRU cache
        """
        super().__init__()
        self.queue = []  # To keep track of access order

    def put(self, key, item):
        """ Add an item in the cache (LRU algorithm)
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get the least recently used key (first element in the queue)
                discarded_key = self.queue.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            # Move the accessed key to the end of the queue-most recently-used
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
