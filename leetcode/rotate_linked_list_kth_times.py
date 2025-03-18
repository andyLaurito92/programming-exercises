class Node:
    @classmethod
    def build_from(clss, a: list[int]) -> 'Node':
        if len(a) == 0:
            raise ValueError("Expecting at least 1 element, got 0")

        root = Node(a[0])
        curr = root
        for x in a[1:]:
            curr.next = Node(x)
            curr = curr.next
        return root
            
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        curr = self
        elements = []
        while curr is not None:
            elements.append(str(curr.value))
            curr = curr.next
        return " -> ".join(elements)

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        else:
            return self.value == other.value and self.next == other.next





root = Node.build_from([1, 2, 3, 4, 5])
print(root)

def rotate_kth(root: Node, k: int):
    old_root = root

    curr = root
    prev = root
    while k != 0 and curr is not None:
        prev = curr
        curr = curr.next
        k -= 1

    if curr is None:
        # Cannot apply kth rotation when k is greater than list
        return root

    new_last = prev
    new_last.next = None
    new_root = curr
    while curr.next is not None:
        curr = curr.next 

    curr.next = old_root
    return new_root


new_root = rotate_kth(root, 3)
print(new_root)


"""
Constraints:
- The number of nodes in the list is in the range [0, 500].
- 100 <= Node.val <= 100
- 0 <= k <= 2 * 109
"""
def rotateRight(root: Node, k: int):
    """
    Given the head of a linked list, rotate the list to the right by k places.
    """

    # First thing because the list is not big, let's calculate it's len
    size = 0
    curr = root
    while curr.next is not None:
        size += 1
        curr = curr.next
    size += 1
    last_element = curr

    k = k % size # real number of rotations to perform

    if k == 0:
        return root # no rotation needed

    new_root_count = size - k
    curr = root
    prev = curr
    while new_root_count != 0:
        prev = curr
        curr = curr.next
        new_root_count -= 1

    new_root = curr
    prev.next = None
    last_element.next = root

    return new_root


list1 = Node.build_from(list(range(1,6)))
rotated = rotateRight(list1, 2)

assert Node.build_from([4, 5, 1, 2, 3]) == rotated
