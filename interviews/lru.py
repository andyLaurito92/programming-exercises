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




"""
Let's now say that we do not have a small capacity. We need to be efficient on
our operations: What could we do?

Idea: Keep in a double linked list the least recently used keys. Every time you
need to evict, you use this linked list to get the key that needs to be removed
from the dict which is the first node

For getting a value, we need to update the timestamp of a node in the list. The
trick here is to store in the dictionary the node of the linked list. By doing this,
we access the node in O(1). This node we move it to the end of the list in O(1) operation.
"""


class Node:
    """
    Implements a double linked list
    """
    def __init__(self, key: int, value:int, timestamp: datetime):
        self.key = key
        self.value = value
        self.timestamp = timestamp
        self.prev = None
        self.thenext = None


class DoubleLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def addLast(self, key: int, value: int, timestamp: datetime) -> None:
        if self.first is None:
            self.first = Node(key, value, timestamp)
            self.last = self.first

        new = Node(key, value, timestamp)
        self.last.thenext = new
        new.prev = self.last
        self.last = new

        return new

    def removeFirst(self):
        if self.first is None:
            raise ValueError("Cannot remove from an empty list")
        removed = self.first
        self.first = self.first.thenext
        self.first.prev = None
        return removed

    def move_to_end(self, node):
        """
        Strong assumption: The node belongs to the list, therefore
        the list contains at least one element
        """
        if self.first == self.last and self.first == node:
            """
            This is the only element in the list, nothing
            to do
            """
            return
        elif self.last == node:
            """
            Element is already the last one, nothing to do
            """
            return
        elif self.first == node:
            self.first = self.first.next
            self.first.prev = None
            self.last.next = node
        else:
            prev = node.prev
            after = node.thenext
            prev.thenext = after
            after.prev = prev
            self.last.next = node


"""
Runtime complexity:
- put: O(1) because
	- adding an element in a dictionary is O(1)
	- removing the first element of a linked list is also O(1)
	- removing an element from a dictionary is O(1)
	- adding a new node as the last element of the linked list is O(1)
- get: O(1) because
	- move_to_end is a constant operation
	- accessing a key in the dictionary is O(1)
Memory:
- You need an additional linked list to keep track of what node to delete next, so
O(N) where N is the number of elements in the cache
"""
class LRU:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._currcap = 0
        self._lru = dict()
        self._keys = DoubleLinkedList()

    def put(self, key: int, value: int) -> None:
        if self._currcap == self._capacity:
            node = self._keys.removeFirst()
            del self._lru[node.key]
            self._currcap -= 1

        node = self._keys.addLast(key, value, datetime.now())
        self._lru[key] = node
        self._currcap += 1

    def get(self, key: int) -> Optional[int]:
        node = self._lru.get(key, None)
        if node is None:
            return None
        else:
            self._keys.move_to_end(node)
            return node.value


class TestLRU(TestCase):
    def test_WhenCapacityFull_GivenPut_ThenleastRecentlyUsedRemoved(self):
        lru = LRU(3)  #LRUSmall(3)

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
        lru = LRU(10)  # LRUSmall(10)

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



"""
Conclustion:
- Even though the exercise sound as heap :) it can be solved easily with a
double linked list and by storing the node in the dictionary
- Think of storing objects that can help you w/the problem u need to solve
(store a node instead of a key-value pair)
- The timestamp is implicit in the double linked list structure: Every time
you do a get/put operation, you are updating a (key, value) pair which means
move the node to the last. For evicting, just remove the first node
"""



"""
To remember: The different types of caches you have:
- LRU: Least recently used
- MRU: Most recently used
- FIFO
- LIFO
- MFU: Most frequenty used
"""
