class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: TreeNode) -> int:
    # Base case: if root is None, return 0
    if not root:
        return 0
    
    # Recursively calculate the maximum depth of the left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    # Return the maximum depth of the left and right subtrees plus 1 (for the current node)
    return max(left_depth, right_depth) + 1

# Helper function to create a binary tree from a list
def create_binary_tree(lst):
    if not lst:
        return None
    
    # Create the root node with the first element of the list
    root = TreeNode(lst[0])
    
    # Use a queue to keep track of the nodes to be processed
    queue = [root]
    
    i = 1
    while i < len(lst):
        # Process the next element in the list
        node = queue.pop(0)
        
        # If the element is not None, create a left child node and add it to the queue
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        
        i += 1
        
        # If there are more elements in the list and the next element is not None,
        # create a right child node and add it to the queue
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        
        i += 1
    
    return root


def test_max_depth():
    # Create a binary tree [3, 9, 20, None, None, 15, 7]
    root = create_binary_tree([3, 9, 20, None, None, 15, 7])
    
    # Test the max_depth function with the created tree
    assert max_depth(root) == 3

def test_max_depth_empty_tree():
    # Create an empty binary tree
    root = create_binary_tree([])
    
    # Test the max_depth function with the empty tree
    assert max_depth(root) == 0

def test_max_depth_single_node():
    # Create a binary tree with a single node
    root = create_binary_tree([1])
    
    # Test the max_depth function with the single node tree
    assert max_depth(root) == 1

def test_max_depth_unbalanced_tree():
    # Create an unbalanced binary tree [1, 2, 3, 4, None, None, None, 5]
    root = create_binary_tree([1, 2, 3, 4, None, None, None, 5])
    
    # Test the max_depth function with the unbalanced tree
    assert max_depth(root) == 4

if __name__ == "__main__":
    # Run the test functions
    test_max_depth()
    test_max_depth_empty_tree()
    test_max_depth_single_node()
    test_max_depth_unbalanced_tree()
    
    # Print a message if all tests passed
    print("All tests passed")
