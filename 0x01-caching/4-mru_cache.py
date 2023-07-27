#!/usr/bin/env python3
"""
Create a class MRUCache that inherits from BaseCaching and is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class Node:
    """ Node class for doubly linked list
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and implements MRU caching
    """

    def __init__(self):
        """ Initialize the MRU cache
        """
        super().__init__()
        self.head = None
        self.tail = None

    def _move_to_front(self, node):
        """ Move the accessed node to the front of the linked list (MRU)
        """
        if node == self.head:
            return

        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

    def put(self, key, item):
        """ Add an item in the cache (MRU algorithm)
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get the most recently used key (the head of the linked list)
                discarded_key = self.head.key
                del self.cache_data[discarded_key]
                self.head = self.head.next
                if self.head:
                    self.head.prev = None

                print("DISCARD:", discarded_key)

            new_node = Node(key, item)
            self.cache_data[key] = new_node

            if self.head is None:
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            node = self.cache_data[key]
            self._move_to_front(node)
            return node.value
        return None
