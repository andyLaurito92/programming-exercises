""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

class TreeNode:
    @classmethod
    def createFrom(clss, mylist) -> 'TreeNode':
        """
        Creates a BST from the provided list
        """
        if len(mylist) == 0:
            raise ValueError("Expected at least one element")
        
        root = TreeNode(mylist[0])
        for i in range(1, len(mylist)):
            root.insert(mylist[i])

        return root

    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, val):
        curr = self
        while True:
            if val < curr.data:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    break
                else:
                    curr = curr.right


""" 
        11
      8         20
   3      9
    11   7
     
  root = 8, less_than = 8, greater_than = 8, left = 3, right = None
      3 <= 8 and 8 < 3
      
"""
from functools import reduce
from operator import and_


"""
Try 1: using 2 lists to try to keep less values and greater values
"""
def check_binary_search_tree_(root):
    def check_binary_tree_rec(curr, less_than, greater_than):
        if curr is None:
            return True

        left = curr.left
        right = curr.right
        curr_value = curr.data

        
        if left is None and right is None:
            return (
                (len(less_than) == 0 or reduce(and_, [curr_value <= x for x in less_than])) and
                (len(greater_than) == 0 or reduce(and_, [x < curr_value for x in greater_than]))
            )
        elif left is None:
            # right is not None and curr is not None
            return (curr_value < right.data and
                (len(less_than) == 0 or reduce(and_, [curr_value <= x for x in less_than])) and
                (len(greater_than) == 0 or reduce(and_, [x < curr_value for x in greater_than])) and
                check_binary_tree_rec(right, less_than, greater_than + [curr_value])
               )
        elif right is None:
            # left is not None and curr is not None
            return (left.data <= curr_value and 
                (len(less_than) == 0 or reduce(and_, [curr_value <= x for x in less_than])) and
                (len(greater_than) == 0 or reduce(and_, [x < curr_value for x in greater_than])) and
                check_binary_tree_rec(left, less_than + [curr_value], greater_than)
               )
        else:
            return (left.data <= curr_value and 
                    curr_value < right.data and
                    (len(less_than) == 0 or reduce(and_, [curr_value <= x for x in less_than])) and
                    (len(greater_than) == 0 or reduce(and_, [curr_value < x for x in greater_than])) and
                    check_binary_tree_rec(left, less_than + [curr_value], greater_than) and 
                    check_binary_tree_rec(right, less_than, greater_than + [curr_value])
                   )
    
    return check_binary_tree_rec(root, [], [])

"""
Try 2. If it's a bst, then applying an inorder search must give a sorted array without duplicates
"""

def check_binary_search_tree_(root):
    def issorted(a):
        """
        Checks if list is sorted in non-decreasing order
        """
        # 0 1 2 -1 2 3 4 
        for i in range(1, len(elements)):
            if a[i - 1] > a[i]:
                return False
        return True

    def noduplicates(a):
        for i in range(1, len(a) - 1):
            if a[i - 1] == a[i]:
                return False
        return True
        
    def inorder(curr, elements):
        if curr is None:
            return elements
        else:
            return inorder(curr.left, elements) + [curr.data] + inorder(curr.right, elements)

    elements = inorder(root, [])
    return issorted(elements)


    


root = TreeNode(8)
root.left = TreeNode(11)
root.right = TreeNode(7)
assert check_binary_search_tree_(root) == False


# 1 2 3 4 5 6 7

root = TreeNode.createFrom(list(range(8)))
assert check_binary_search_tree_(root) == True

"""
      8
    4
  -3  11
"""
root = TreeNode(8)
root.left = TreeNode(4)
root.left.right = TreeNode(11)
root.left.left = TreeNode(-3)

assert check_binary_search_tree_(root) == False


"""
Moral here: Know the properties of BST because it makes your life easy :)
"""
