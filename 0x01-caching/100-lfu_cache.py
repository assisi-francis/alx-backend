#!/usr/bin/env python3
"""
Create a class LFUCache that inherits from BaseCaching and is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and implements LFU caching
    """

    def __init__(self):
        """ Initialize the LFU cache
        """
        super().__init__()
        self.frequency = {}  # To keep track of item frequencies
        self.min_frequency = 0  # To keep track of the minimum frequency

    def put(self, key, item):
        """ Add an item in the cache (LFU algorithm)
        """
        if key is not None and item is not None:
            if BaseCaching.MAX_ITEMS <= 0:
                return

            # If key already exists, update the item and increase its frequency
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
            else:
                # If the cache is full, remove least frequency used items (LFU)
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    self._discard_least_frequency_used()

                self.cache_data[key] = item
                self.frequency[key] = 1
                self.min_frequency = 1

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            # Update the frequency and find the new minimum frequency
            self.frequency[key] += 1
            self.min_frequency = min(self.frequency.values())

            return self.cache_data[key]
        return None

    def _discard_least_frequency_used(self):
        """ Discard the least frequency used items (LFU) """
        if self.cache_data:
            items_to_discard = [key for key, freq in self.frequency.items() if freq == self.min_frequency]

            if len(items_to_discard) == 1:
                discarded_key = items_to_discard[0]
            else:
                # If there are multiple items with the same minimum frequency,
                # discard the least recently used (LRU) among them
                discarded_key = min(items_to_discard, key=lambda k: self.cache_data[k])

            del self.cache_data[discarded_key]
            del self.frequency[discarded_key]
            print("DISCARD:", discarded_key)
