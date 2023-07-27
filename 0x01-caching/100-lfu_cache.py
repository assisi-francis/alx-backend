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
        self.fre = {}  # To keep track of item frequencies
        self.min_fre = 0  # To keep track of the minimum frequency

    def put(self, key, item):
        """ Add an item in the cache (LFU algorithm)
        """
        if key is not None and item is not None:
            if BaseCaching.MAX_ITEMS <= 0:
                return

            # If key already exists, update the item and increase its frequency
            if key in self.cache_data:
                self.cache_data[key] = item
                self.fre[key] += 1
            else:
                # If the cache is full, remove least frequency used items (LFU)
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    self._discard_least_frequency_used()

                self.cache_data[key] = item
                self.fre[key] = 1
                self.min_fre = 1

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            # Update the frequency and find the new minimum frequency
            self.fre[key] += 1
            self.min_fre = min(self.fre.values())

            return self.cache_data[key]
        return None

    def _discard_least_frequency_used(self):
        """ Discard the least frequency used items (LFU) """
        if self.cache_data:
            i_to_d = [k for k, f in self.fre.items() if f == self.min_fre]

            if len(i_to_d) == 1:
                discard_key = i_to_d[0]
            else:
                # If there are multiple items with the same minimum frequency,
                # discard the least recently used (LRU) among them
                discard_key = min((k for k in i_to_d), key=self.cache_data.get)

            del self.cache_data[discard_key]
            del self.fre[discard_key]
            print("DISCARD:", discard_key)
