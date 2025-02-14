"""
Given an integer array numbers, return the 2th largest element in the array.
Example: [3,2,1,5,6,4] -> 5

Requirements:
   1) The function is expected to return an Integer.
   2) The function accepts an Integer array numbers as parameter.
"""

from typing import Optional


# 5, 5, 2
# x = 5, max_value = -99, second_largest = -99
# 1 2 2 3
def second_largest(mylist: list[int]) -> Optional[int]:
    n = len(mylist)
    if n == 0 or n == 1:
        return None

    myset = set(mylist)
    max_val = max(myset)
    myset.remove(max_val)

    return max(myset)


def second_largest2(mylist: list[int]) -> Optional[int]:
    max_value = -99
    second_largest = -99

    for x in mylist:
        if x > max_value:
            second_largest = max_value
            x = max_value

        if second_largest < x and x < max_value:
            x = second_largest

    return second_largest

class MyHeap:
    def __init__(self, elements: list[int] | None = None):
        self.elements = [] if elements is None else elements.copy()
        self.n = len(elements)
        self.heapify()

    def sink(self, k: int) -> None:
        while 2 * k + 1 < self.n:
            highest_child = 2 * k + 1
            if 2*k + 2 < self.n and self.elements[2*k + 2] > self.elements[2*k + 1]:
                highest_child = 2*k + 2

            if self.elements[k] < self.elements[highest_child]:
                self.elements[k], self.elements[highest_child] = self.elements[highest_child], self.elements[k]
                k = highest_child
            else:
                return

    def swim(self, k: int) -> None:
        while k > 0:
            parent = k // 2
            if self.elements[parent] < self.elements[k]:
                self.elements[parent], self.elements[k] = self.elements[k], self.elements[parent]
            k = k // 2
   
                

    def max(self) -> int:
        if self.n == 0:
            raise ValueError("Empty heap")

        max_val = self.elements[0]
        if self.n - 1 == 0:
            del self.elements[0]
            return max_val

        self.elements[0] = self.elements[self.n - 1]
        self.sink(0)
        del self.elements[self.n - 1]
        self.n -= 1
        return max_val


    def heapify(self):
        """
        Important note: This heapify takes O(N) to run and it's
        based on the fact that we just need to create heaps
        starting from the first non-leaf node and keep iterating
        until the root (bottom-up approach). If we follow the top-down
        approach, this is, to swim up elements from the last leaf node
        then the complexity is close to O(N * log N)

        See these articles about this:
        1 - https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/
        2 - https://www.geeksforgeeks.org/building-heap-from-array/
        """
        for i in reversed(range(self.n//2)):
            self.sink(i)

        

def second_largest3(mylist: list[int], k: int = 2) -> Optional[int]:
    """
    Generalization of the problem of getting the second largest. Getting the
    2th largest can be generalised to getting the kth largest from a list.
    This can be implemented by using a heap instead of a list.
    In order to build the heap from the list, we use the heapify algorithm
    which takes O(N) runtime
    """
    myheap = MyHeap(mylist)
    kth_largest = myheap.max()
    k -= 1 # max_val is the 1st largest element
    if k == 0:
        return kth_largest # k = 1 meaning max value

    while k != 0:
        next_largest = myheap.max()
        if next_largest != kth_largest: # myheap can have duplicates
            k -= 1
            kth_largest = next_largest
    return kth_largest
