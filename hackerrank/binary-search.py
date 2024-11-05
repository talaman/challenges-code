# Objective: Given a binary tree, print the level order traversal of the tree -
# that is, the nodes at each level from left to right.
#
# Task: Implement the levelOrder function in the editor below.
#
# levelOrder has the following parameter(s):
#
# Node root: a reference to the root of a binary tree
#
# Print the values in a single line separated by a space.
#
# Input Format
#
# You do not need to read any input from stdin. Our grader will pass the root node of a binary tree to your levelOrder function.
#
# Constraints
#
# 1 <= Nodes in the tree <= 500
#
# Output Format
#
# Print the values on a single line separated by space.
#
# Sample Input
#
#      1
#       \
#        2
#         \
#          5
#         /  \
#        3    6
#         \
#          4
#
# Sample Output
#
# 1 2 5 3 6 4
#
# Explanation
#
# We need to print the nodes level by level. We process each level from left to right.
# Level Order Traversal: 1 -> 2 -> 5 -> 3 -> 6 -> 4
#
# Approach:
# The level order traversal of a binary tree can be done using a queue data structure.
# We start by adding the root node to the queue.
# We then enter a loop where we dequeue a node from the queue, print its value, and enqueue its children.
# We continue this process until the queue is empty.
# The time complexity of this approach is O(n), where n is the number of nodes in the binary tree.
# The space complexity is also O(n) in the worst case, where all nodes are at the last level of the tree.

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.info, end=' ')
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)