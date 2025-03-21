"""
Find the lowest common ancestor in a BST

Note: This is easier bc of how a bst is built
Complexity arises when we need to find a lca of whatever type of tree
"""

class TreeNodeBST:
    @classmethod
    def createFrom(clss, elements: list[int]) -> 'TreeNode':
        n = len(elements)
        if n == 0:
            raise ValueError("BST must have at least one element")

        root = TreeNodeBST(elements[0])
        for i in range(1, n):
            root.insert(elements[i])

        return root

    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.value = val

    def __str__(self):
        # 5 6 7
        mylevel = self.height()
        space = " " * 2 * mylevel
        left = "" if self.left is None else str(self.left)
        right = "" if self.right is None else str(self.right)
        return f"{space} {self.value} \n {left} {space} {right}"


    def height(self):
        left_height = 0 if self.left is None else self.left.height()
        right_height = 0 if self.right is None else self.right.height()
        return 1 + max(left_height, right_height)
        
    def insert(self, val: int) -> None:
        curr = self
        while True:
            if curr.value < val:
                # go right
                if curr.right is None:
                    curr.right = TreeNodeBST(val, None, None)
                    break
                else:
                    curr = curr.right
            else:
                # go to left
                if curr.left is None:
                    curr.left = TreeNodeBST(val, None, None)
                    break
                else:
                    curr = curr.left

        
    def lowest_common_ancestor_bst(self, v1: int, v2:int) -> int:
        """
        Return the lowest common ancestor between v1 and v2

        Strong assumption: lca exists
        This computes the lca in a BST! not a BT
        """

        # lowest common ancestor of root is root
        if self.value == v1 or self.value == v2:
            return self.value

        if v2 < v1:
            v1, v2 = v2, v1

        curr = self
        while True:
            if v1 <= curr.value and curr.value < v2:
                return curr.value
            elif curr.value < v1 and curr.value < v2:
                curr = curr.right
            else:
                curr = curr.left



"""
TODO: Review algorithm that uses union find to find the lca
"""
class UnionFind:
    def __init__(self, n: int) -> None:
        self.count = n
        self.elements = [i for i in range(n)]

    def union(self, p: int, q: int) -> None:
        u1 = self.find(p)
        u2 = self.find(q)

        if u1 == u2:
            return
        else:
            self.elements[u1] = u2
            self.count -= 1

    def count(self) -> int:
        return self.count
        
    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)
        
    def find(self, p: int) -> int:
        curr = p
        while self.elements[curr] != curr:
            curr = self.elements[curr]
        return curr
        

elements = [4,2,3,1,7,6]
root = TreeNodeBST.createFrom(elements)
assert 4 == root.lowest_common_ancestor_bst(1, 7)

elements = [2, 1, 3, 4, 5, 6]
root = TreeNodeBST.createFrom(elements)
assert 4 == root.lowest_common_ancestor_bst(4, 6)

print(TreeNode.createFrom([5, 6, 7]))


"""
Another approach: Just use dfs in a graph
"""

from collections import deque

class TreeNode:
    value: int
    left: 'TreeNode'
    right: 'TreeNode'

    @classmethod
    def createFrom(clss, values: list[int]) -> 'TreeNode':
        """
        Creates a BT from the given values. The way of creating
        it is by creating a complete BT, which means that if you want
        it not to be a complete BT, you need to provide None values
        to fill the gaps
        """
        n = len(values)
        if n == 0:
            raise ValueError("Expected at least one element")

        root = TreeNode(values[0])
        nextnode = deque()
        nextnode.append(root)
        for i in range(1, n - 1, 2):
            curr = nextnode.popleft()
            curr.left = TreeNode(values[i])
            curr.right = TreeNode(values[i+1])

            nextnode.append(curr.left)
            nextnode.append(curr.right)
        return root

    def lowest_common_ancestor(self, v1:int, v2:int) -> int:
        """
        Returns the lowest common ancestor between v1 and v2

        Strong assumption: Both v1 and v2 exists

        Runtime complexity: Worst case scenario -> We have the
        longest path for both vertices. Longest path is O(log N)
        (size of the tree)
        dfs = O(N) where N = number of vertices
        find common lowest ancestor = O((log N)^2) Per each vertex
        in the path, go and see if it belongs to the other path
        => O(N + logN ^2)
        """
        if self.value == v1 or self.value == v2:
            return self.value

        def find(curr: 'TreeNode', path: list[int], tofind: int) -> (list['TreNode'], bool):
            path.append(curr)
            if curr.value == tofind:
                return path, True

            if curr.left is not None:
                path, found = find(curr.left, path, tofind)
                if found:
                    return path, True
            if curr.right is not None:
                path, found = find(curr.right, path, tofind)
                if found:
                    return path, True

            path.pop()
            return path, False

        path_to_v1, found = find(self, [], v1)

        if not found:
            raise ValueError(f"Expected to find {v1} but it wasn't found")

        path_to_v2, found = find(self, [], v2)
        if not found:
            raise ValueError(f"Expected to find {v1} but it wasn't found")


        i = len(path_to_v1) - 1
        while True:
            if path_to_v1[i] in path_to_v2:
                return path_to_v1[i].value
            i -= 1


    def __repr__(self):
        return str(self.value)

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


"""
These are not bsts
"""
elements = [5, 3, 8, 2, 4, 6, 7]
root = TreeNode.createFrom(elements)

assert 5 == root.lowest_common_ancestor(7, 3)


elements = [23, 16, 15, 9, 6, 17, 10, 13, 8, 26, 18, 2, 22, 24, 12, 5, 20, 25, 21, 4, 19, 1, 3, 14, 7]
root = TreeNode.createFrom(elements)
assert 23 == root.lowest_common_ancestor(23, 3)
