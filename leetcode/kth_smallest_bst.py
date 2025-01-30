"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Constraints:

    The number of nodes in the tree is n.
    1 <= k <= n <= 104
    0 <= Node.val <= 104

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import heapify, heappop, heappush

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None or k is 0:
            return 0

        smallest = root.val
        to_visit = [root]
        elements = []
        while len(to_visit) > 0:
            current = to_visit.pop()
            if current is not None:
                elements.append(current.val)
                to_visit.extend((current.left, current.right))
        
        heapify(elements)
        smallest = None
        while k > 0:
            smallest = heappop(elements)
            k -= 1
        return smallest
        
