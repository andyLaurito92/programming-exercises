"""
Design and implement a data structure for Least Recently Used (LRU) cache. 
It should support the following operations: get(key) and put(key,value) where key is an integer and value is a positive integer.
 
 
get(key) Get the value of the key if the key exists in the cache, otherwise return something indicating that it’s missing.
put(key, value) Set the value if the key is not already present or update it if it is. When the cache is at capacity, (i.e., it is full), it should evict (i.e., remove) the Least Recently Used item before inserting a new item.
 
 
The cache is initialized with a positive capacity
"""

"""
First thing to think about: If capacity is a small-medium number, then it means that we might consider
a constant time to go through the whole lru cache! If that is the case, then the easiest thing to do
is just to use a normal dict and evict in linear time
"""

from typing import Optional
from datetime import datetime

from unittest import TestCase


class LRUSmall:
    """
    Implements least recently used cached using a dict and assuming capacity
    is small, meaning that we don't really care on iterating throught the whole
    data structure every time we need to evict
    """
    def __init__(self, capacity):
        self._lru = dict()
        self._currcap = 0
        self._capacity = capacity

    def get(self, key: int) -> Optional[int]:
        val = self._lru.get(key, None)
        if val is not None:
            res, _ = val
            self._lru[key] = (res, datetime.now())
            return res

    def put(self, key: int, val: int) -> None:
        if self._currcap == self._capacity:
            self._evict()

        if key not in self._lru:
            self._currcap += 1

        self._lru[key] = (val, datetime.now())

    def _evict(self):
        """
        Removes least recently used value
        """
        to_remove = None
        for key, (_, put_time) in self._lru.items():
            if to_remove is None:
                to_remove = (key, put_time)
            elif to_remove[1] > put_time:
                to_remove = (key, put_time)

        key, _ = to_remove
        del self._lru[key]
        self._currcap -= 1


class TestLRUSmall(TestCase):
    def test_WhenCapacityFull_GivenPut_ThenleastRecentlyUsedRemoved(self):
        lru = LRUSmall(3)

        lru.put(1, 10)
        lru.put(2, 20)
        lru.put(3, 30)

        self.assertEqual(lru.get(1), 10)
        self.assertEqual(lru.get(2), 20)
        self.assertEqual(lru.get(3), 30)

        lru.put(4, 40)

        self.assertEqual(lru.get(2), 20)
        self.assertEqual(lru.get(3), 30)
        self.assertEqual(lru.get(4), 40)

        self.assertFalse(lru.get(1))

    def test_WhenStillCapacity_GivenPut_NothingRemoved(self):
        lru = LRUSmall(10)

        lru.put(1, 10)
        lru.put(2, 20)
        lru.put(3, 30)

        self.assertEqual(lru.get(1), 10)
        self.assertEqual(lru.get(2), 20)
        self.assertEqual(lru.get(3), 30)

        lru.put(4, 40)

        self.assertEqual(lru.get(1), 10)
        self.assertEqual(lru.get(2), 20)
        self.assertEqual(lru.get(3), 30)
        self.assertEqual(lru.get(4), 40)
