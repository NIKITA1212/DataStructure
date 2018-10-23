class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def inOrderSuccessor(root, n):
    # Step 1 of the above algorithm
    if n.right is not None:
        return minValue(n.right)

    # Step 2 of the above algorithm
    p = n.parent
    while (p is not None):
        if n != p.right:
            break
        n = p
        p = p.parent
    return p


# Given a non-empty binary search tree, return the
# minimum data value found in that tree. Note that the
# entire tree doesn't need to be searched
def minValue(node):
    # loop down to find the leftmost leaf
    current = node
    while current.left is not None:
        current = current.left

    return current

root = Node(12)
root.left = Node(8)
root.right = Node(13)
root.left.left = Node(6)
root.left.right = Node(9)
root.left.right.right = Node(10)
#root.left.right.right.right = Node(11)
temp = root.left.left

succ = inOrderSuccessor(root, temp)
if succ is not None:
    print("\nInorder Successor of %d is %d " % (temp.data, succ.data))
else:
    print("\nInorder Successor doesn't exist")