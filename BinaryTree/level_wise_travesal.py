# Define a Node class to represent each node in the tree
from collections import deque


class Node:
    def __init__(self, data) -> None:
        self.data = data          # Store the node's data
        self.left = None          # Initialize left child as None
        self.right = None         # Initialize right child as None

# Define the BinaryTree class to manage the tree and its operations
class BinaryTree:
    def __init__(self) -> None:
        self.root = None          # Start with an empty tree (no root)

    # Insert a new node into the binary tree
    def insert(self, data):
        # If the tree is empty, make this node the root
        if self.root is None:
            self.root = Node(data)
        else:
            # Otherwise, find the correct place for the new node
            self._insert(self.root, data)

    # Helper function to handle the insertion logic recursively
    def _insert(self, current, data):
        # If the new data is less than the current node's data, go left
        if data < current.data:
            # If there's no left child, place the new node here
            if current.left is None:
                current.left = Node(data)
            else:
                # Recursively move left to find the correct position
                self._insert(current.left, data)
        # If the new data is greater, go right
        elif data > current.data:
            # If there's no right child, place the new node here
            if current.right is None:
                current.right = Node(data)
            else:
                # Recursively move right to find the correct position
                self._insert(current.right, data)
        

    # level wise traversal
    from collections import deque
    def level_wise_traversal(self):
        if self.root:
            return self.bfs(self.root)
    def bfs(self,root):
        if root is None:
            return

        queue = deque([root])  # Initialize the queue with the root node

        while queue:
            node = queue.popleft()  # Dequeue the front node
            print(node.data, end=" ")  # Process the current node

            if node.left:  # Enqueue left child
                queue.append(node.left)
            if node.right:  # Enqueue right child
                queue.append(node.right)


bst = BinaryTree()

# Insert some values into the tree
bst.insert(10)
bst.insert(45)
bst.insert(34)
bst.insert(45)  # Duplicate value (handled by ignoring it in this implementation)
bst.insert(2)
bst.insert(1)
bst.insert(5)
bst.insert(11)
bst.insert(22)
bst.insert(13)
bst.insert(4)



# level wise traversal
bst.level_wise_traversal()
