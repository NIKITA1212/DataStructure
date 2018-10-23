
class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#print("Simple but wrong")
def binaryIsBST(root):
    if root is None:
        return True

    if root.left is not None and (root.left.data <root.data) :
        binaryIsBST(root.left)
    elif root.right is not None and root.right.data > root.data:
        binaryIsBST(root.right)
    else:
        return False
    return True

"""" above code will not give you right answer for below tree
   3
  / \
  2   5 
 / \
1   4
"""


INT_MAX = 4294967296
INT_MIN = -4294967296

# Returns true if the given tree is a binary search tree
# (efficient version)
def isBST(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))


# Retusn true if the given tree is a BST and its values
# >= min and <= max
def isBSTUtil(node, mini, maxi):
    # An empty tree is BST
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.data - 1) and
            isBSTUtil(node.right, node.data + 1, maxi))



root = Node(12)
root.left = Node(8)
root.right = Node(13)
root.left.left = Node(6)
root.left.right = Node(9)
root.left.right.right = Node(10)
root.left.right.right.right = Node(11)
result = binaryIsBST(root)
if result == True:
    print("Method1(Not true for all cases) Binary Tree is BST")
else:
    print("Method1 (Not true for all cases) Binary Tree is not BST")

if (isBST(root)== True):
    print("Method2: Is BST")
else:
    print("Method2: Not a BST")
