# Python code to convert a sorted array
# to a balanced Binary Search Tree

# binary tree node
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


# function to convert sorted array to a
# balanced BST
# input : sorted array of integers
# output: root node of balanced BST
def sortedArrayToBST(arr):
    if not arr:
        return None

    # find middle
    mid = (len(arr)) // 2  #integer division

    # make the middle element the root
    root = Node(arr[mid])

    # left subtree of root has all
    # values <arr[mid]
    root.left = sortedArrayToBST(arr[:mid])

    # right subtree of root has all
    # values >arr[mid]
    root.right = sortedArrayToBST(arr[mid + 1:])
    #print(root.data)
    return root


# A utility function to print the preorder
# traversal of the BST

def preOrder(node,porder = []):
    if not node:
        return
    porder.append(node.data)
    preOrder(node.left)
    preOrder(node.right)

    return porder

def postOrder(node,ptorder = []):
    if not node:
        return
    postOrder(node.left)
    postOrder(node.right)
    ptorder.append(node.data)
    return ptorder


def inOrder(node,inorder = []):
    if not node:
        return
    inOrder(node.left)
    inorder.append(node.data)
    inOrder(node.right)

    return inorder

arr = [1, 2, 3, 4, 5, 6, 7, 8]
root = sortedArrayToBST(arr)
print("PreOrder Traversal of constructed BST :- {}".format(preOrder(root)))
print("PostOrder Traversal of constructed BST :- {}".format(postOrder(root)))
print("InOrder Traversal of constructed BST :- {}".format(inOrder(root)))


