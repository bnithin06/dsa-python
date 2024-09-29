# Define a Node class to represent each node in the tree
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

    # Pre-order traversal: visit root, left subtree, then right subtree
    def pre_order(self):
        self._pre_order(self.root)    # Start traversal from the root

    # Recursive function to handle pre-order traversal
    def _pre_order(self, current):
        if current is None:
            return
        # Visit current node first (root)
        print(current.data, end=' ')
        # Traverse the left subtree
        self._pre_order(current.left)
        # Traverse the right subtree
        self._pre_order(current.right)

    # Post-order traversal: visit left subtree, right subtree, then root
    def post_order(self):
        self._post_order(self.root)   # Start traversal from the root

    # Recursive function to handle post-order traversal
    def _post_order(self, current):
        if current is None:
            return
        # Traverse the left subtree first
        self._post_order(current.left)
        # Traverse the right subtree
        self._post_order(current.right)
        # Visit current node last (root)
        print(current.data, end=' ')

    # Recursive functionn to handle in-order traversal
    def in_order(self):
        self._in_order(self,self.root)

    def _in_order(self,current):
        if current is None:
            return
        self._in_order(current.left)
        print(current.data,end=' ')
        self._in_order(current.right)
    

    # Search for a specific value in the binary tree
    def search(self, Target):
       self._search(self.root, Target)   # Start search from the root

    # Recursive function to handle the search operation
    def _search(self, current, Target):
        if current is None:
            print(False)    # Target not found if we've reached a leaf
            return
        if current.data == Target:
            print(True)     # Target found at the current node
            return
        # If target is less than current node's data, search in the left subtree
        if Target < current.data:
            self._search(current.left, Target)
        # If target is greater, search in the right subtree
        elif Target > current.data:
            self._search(current.right, Target)

# Let's create a binary search tree (BST) instance
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

# Perform pre-order traversal to print the nodes in pre-order sequence
bst.pre_order()  
print()

# Perform post-order traversal to print the nodes in post-order sequence
bst.post_order()
print()

#  Perform In-order traversal to print the nodes in In-order sequence
#  the nodes are present in sorted order


# Perform some search operations to check if specific values exist in the tree
bst.search(45)   # Should print True
bst.search(11)   # Should print True
bst.search(23)   # Should print False (23 is not in the tree)
bst.search(22)   # Should print True
