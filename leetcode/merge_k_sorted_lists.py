"""
You are given an array of k linked-lists lists, each linked-list is sorted
in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # idx of each sublist
        n = len(lists)
        if n == 0:
            return None
        
        nexts = [0] * n # first elements
        nones = 0
        minidx = -1
        # init
        for i, sublist in enumerate(lists):
            if sublist is not None:
                nexts[i] = sublist.val
                lists[i] = lists[i].next
                minidx = i
            else:
                nexts[i] = None
                nones += 1

        if nones == n:
            return None
        
        res = ListNode()
        curr = res
        while True:
            # add next elem to res
            curr.val = nexts[minidx]
            curr.next = ListNode()
            prev = curr
            curr = curr.next

            # pump next value from list ith
            if lists[minidx] is not None:
                nexts[minidx] = lists[minidx].val
                lists[minidx] = lists[minidx].next
            else:
                nexts[minidx] = None

            # find min
            minidx = None
            for i, val in enumerate(nexts):
                if minidx is None:
                    if val is not None:
                        minidx = i
                    else:
                        continue

                if val is not None and val < nexts[minidx]:
                    minidx = i

            if minidx is None:
                prev.next = None
                return res # finished
                    
            

            


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Solution 2 uses a min-heap instead of a list to find the minimum. 

The idea is to improve the update of the minimum given that we have a
pretty much stable data structure. Instead of linearly finding the minimum
over all elements, we find the min in O(log(n)) and update the min in O(log(n))
"""

import heapq

class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # idx of each sublist
        n = len(lists)
        if n == 0:
            return None
        
        nexts = [] # first elements
        nones = 0
        # init
        for i, sublist in enumerate(lists):
            if sublist is not None:
                nexts.append((sublist.val, i))
                lists[i] = lists[i].next
            else:
                nones += 1
        if nones == n:
            return None
        
        res = ListNode()
        curr = res
        heapify(nexts)
        while True:
            # find min
            try:
                val, i = heappop(nexts)
            except IndexError:
                # empty heap, finished
                prev.next = None
                return res
        
            # add next elem to res
            curr.val = val
            curr.next = ListNode()
            prev = curr
            curr = curr.next

            # pump next value from list ith
            if lists[i] is not None:
                heappush(nexts, (lists[i].val, i))
                lists[i] = lists[i].next
