# Define a Node class to represent each node in the binary tree
class Node:
    """Node class for binary tree"""
    def __init__(self, value):
        # Initialize a node with a value and two children (left and right)
        self.value = value
        self.left = None
        self.right = None

# Define a BinaryTree class to manage the binary tree
class BinaryTree:
    """Binary Tree class"""
    def __init__(self):
        # Initialize the binary tree with a root node (None initially)
        self.root = None

    # Method to insert a node with a given value into the binary tree
    def insert(self, value):
        # Check if the tree is empty
        if self.root is None:
            # If the tree is empty, set the root node to the new node
            self.root = Node(value)
        else:
            # If the tree is not empty, insert the new node recursively
            self._insert(self.root, value)

    # Helper function to insert a node into the binary tree recursively
    def _insert(self, node, value):
        # Check if the value is less than the current node's value
        if value < node.value:
            # If the left child is empty, insert the new node as the left child
            if node.left is None:
                node.left = Node(value)
            else:
                # If the left child is not empty, insert the new node recursively
                self._insert(node.left, value)
        else:
            # If the value is not less than the current node's value
            # Check if the right child is empty
            if node.right is None:
                # If the right child is empty, insert the new node as the right child
                node.right = Node(value)
            else:
                # If the right child is not empty, insert the new node recursively
                self._insert(node.right, value)

    # Method to perform inorder traversal of the binary tree
    def inorder(self):
        # Check if the tree is not empty
        if self.root is not None:
            # Perform inorder traversal recursively
            self._inorder(self.root)

    # Helper function to perform inorder traversal recursively
    def _inorder(self, node):
        # Check if the node is not None
        if node is not None:
            # Traverse the left child recursively
            self._inorder(node.left)
            # Print the node's value
            print(node.value, end=' ')
            # Traverse the right child recursively
            self._inorder(node.right)

    # Method to perform preorder traversal of the binary tree
    def preorder(self):
        # Check if the tree is not empty
        if self.root is not None:
            # Perform preorder traversal recursively
            self._preorder(self.root)

    # Helper function to perform preorder traversal recursively
    def _preorder(self, node):
        # Check if the node is not None
        if node is not None:
            # Print the node's value
            print(node.value, end=' ')
            # Traverse the left child recursively
            self._preorder(node.left)
            # Traverse the right child recursively
            self._preorder(node.right)

    # Method to perform postorder traversal of the binary tree
    def postorder(self):
        # Check if the tree is not empty
        if self.root is not None:
            # Perform postorder traversal recursively
            self._postorder(self.root)

    # Helper function to perform postorder traversal recursively
    def _postorder(self, node):
        # Check if the node is not None
        if node is not None:
            # Traverse the left child recursively
            self._postorder(node.left)
            # Traverse the right child recursively
            self._postorder(node.right)
            # Print the node's value
            print(node.value, end=' ')


# Example usage
if __name__ == "__main__":
    # Create a binary tree
    tree = BinaryTree()

    # Insert values into the binary tree
    tree.insert(8)
    tree.insert(3)
    tree.insert(10)
    tree.insert(1)
    tree.insert(6)
    tree.insert(14)
    tree.insert(4)
    tree.insert(7)
    tree.insert(13)

    # Perform inorder traversal and print the result
    print("Inorder Traversal:")
    tree.inorder()  # Output: 1 3 4 6 7 8 10 13 14
    print("\n")

    # Perform preorder traversal and print the result
    print("Preorder Traversal:")
    tree.preorder()  # Output: 8 3 1 6 4 7 10 14 13
    print("\n")

    # Perform postorder traversal and print the result
    print("Postorder Traversal:")
    tree.postorder()  # Output: 1 4 7 6 3 13 14 10 8