# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

from typing import Optional
from itertools import zip_longest

# Definition for singly-linked list.

# Note (not related to this exercise): This listnode resembles
# (car cdr) from lisp. With this abstraction, a whole programming
# language has been built :) With this comment I wont to emphasize
# the simplicity and power of this abstractinon

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def listNodeFromList(alist):
    if len(alist) == 0:
        return None

    res = ListNode()
    res.val = alist[0]
    res.next = listNodeFromList(alist[1:])
    return res

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        reminder = 0

        def __iter__(self):
            if self.val is None:
                yield None
            yield self.val
            if self.next is not None:
                yield from iter(self.next)

        ListNode.__iter__ = __iter__

        # Ideal would be to use zip_longest from itertools with fillvalue=0
        for digit1, digit2 in zip_longest(l1, l2, fillvalue=0):
            digitsum = digit1 + digit2 + reminder
            newdigit = digitsum % 10
            reminder = 1 if digitsum >= 10 else 0
            res.append(newdigit)

        if reminder != 0:
            res.append(reminder)

        return res


mysolution = Solution()

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

print(mysolution.addTwoNumbers(l1, l2))

l1 = ListNode(0)
l2 = ListNode(0)

print(mysolution.addTwoNumbers(l1, l2))

l2 = ListNode(0)

print(mysolution.addTwoNumbers(l1, l2))

l1 = listNodeFromList([9, 9, 9, 9, 9, 9, 9])
l2 = listNodeFromList([9, 9, 9, 9])

print(mysolution.addTwoNumbers(l1, l2))
