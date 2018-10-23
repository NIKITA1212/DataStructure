# Python Program for Lowest Common Ancestor in a Binary Tree
# O(n) solution to find LCS of two given values n1 and n2
# A binary tree node
class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Finds the path from root node to given root of the tree.
# Stores the path in a list path[], returns true if path
# exists otherwise false
def findPath(root, path, k):
    # Baes Case
    if root is None:
        return False

    # Store this node is path vector. The node will be
    # removed if not in path from root to k
    path.append(root.key)

    # See if the k is same as root's key
    if root.key == k:
        return True

    # Check if k is found in left or right sub-tree
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right != None and findPath(root.right, path, k))):
        return True

    # If not present in subtree rooted with root, remove
    # root from path and return False

    path.pop()
    return False


# Returns LCA if node n1 , n2 are present in the given
# binary tre otherwise return -1
def findLCA(root, n1, n2):
    # To store paths to n1 and n2 fromthe root
    path1 = []
    path2 = []

    # Find paths from root to n1 and root to n2.
    # If either n1 or n2 is not present , return -1
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1

    # Compare the paths to get the first different value
    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]


# Driver program to test above function
# Let's create the Binary Tree shown in above diagram


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

print("LCA = %d" % (findLCA(root, 4, 14)))
print("LCA = %d" % (findLCA(root, 22, 8)))
print("LCA = %d" % (findLCA(root, 10, 22)))


# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
print("second method")

# Python program to find LCA of n1 and n2 using one
# traversal of Binary tree

# A binary tree node
class Node:

	# Constructor to create a new tree node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

# This function returns pointer to LCA of two given
# values n1 and n2
# This function assumes that n1 and n2 are present in
# Binary Tree
def findLCA(root, n1, n2):

	# Base Case
	if root is None:
		return None

	# If either n1 or n2 matches with root's key, report
	# the presence by returning root (Note that if a key is
	# ancestor of other, then the ancestor key becomes LCA
	if root.data == n1 or root.data == n2:
		return root

	# Look for keys in left and right subtrees
	left_lca = findLCA(root.left, n1, n2)
	right_lca = findLCA(root.right, n1, n2)

	# If both of the above calls return Non-NULL, then one key
	# is present in once subtree and other is present in other,
	# So this node is the LCA
	if left_lca and right_lca:
		return root

	# Otherwise check if left subtree or right subtree is LCA
	return left_lca if left_lca is not None else right_lca


# Driver program to test above function

# Let us create a binary tree given in the above example

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

print("LCA = %d" % (findLCA(root, 4, 14).data))
print("LCA = %d" % (findLCA(root, 22, 8).data))
print("LCA = %d" % (findLCA(root, 10, 22).data))

#root = Node(1)
#root.left = Node(2)
#root.right = Node(3)
#root.left.left = Node(4)
#root.left.right = Node(5)
#root.right.left = Node(6)
#root.right.right = Node(7)
#print("LCA(4,5) = ", findLCA(root, 4, 5).key)
#print("LCA(4,6) = ", findLCA(root, 4, 6).key)
#print("LCA(3,4) = ", findLCA(root, 3, 4).key)
#print("LCA(2,4) = ", findLCA(root, 2, 4).key)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
