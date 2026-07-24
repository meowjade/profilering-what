class Node:
    """Node class for binary tree storing student records."""

    def __init__(self, id: int, name: str):
        """Initialize a new node with student record.

        Args:
            id: Student ID (used as sorting key)
            name: Student name
        """
        # Replace this code with your implementation
        raise NotImplementedError

    def preorder(self) -> list[dict]:
        """Return preorder traversal as list of dicts.

        Returns:
            List of {id, name} dicts in preorder (root, left, right)
        """
        # Replace this code with your implementation
        raise NotImplementedError

    def inorder(self) -> list[dict]:
        """Return inorder traversal as list of dicts.

        Returns:
            List of {id, name} dicts in inorder (left, root, right)
        """
        # Replace this code with your implementation
        raise NotImplementedError

    def postorder(self) -> list[dict]:
        """Return postorder traversal as list of dicts.

        Returns:
            List of {id, name} dicts in postorder (left, right, root)
        """
        # Replace this code with your implementation
        raise NotImplementedError


class Tree:
    """Binary search tree for storing and managing student records."""

    def __init__(self):
        """Initialize an empty tree."""
        self.root = None

    def add(self, id: int, name: str) -> None:
        """Add a new student record to the tree.

        Args:
            id: Student ID (used as sorting key)
            name: Student name

        Note:
            If id already exists, this operation should be ignored.
        """
        # Replace this code with your implementation
        raise NotImplementedError

    def find_node(self, id: int):
        """Find a student node by ID.

        Args:
            id: Student ID to search for

        Returns:
            Node object if found, None otherwise
        """
        # Replace this code with your implementation
        raise NotImplementedError

    def preorder(self) -> list[dict]:
        """Return preorder traversal of tree.

        Returns:
            List of {id, name} dicts in preorder (root, left, right)
        """
        # Replace this code with your implementation
        raise NotImplementedError

    def inorder(self) -> list[dict]:
        """Return inorder traversal of tree.

        Returns:
            List of {id, name} dicts in inorder (left, root, right)
        """
        # Replace this code with your implementation
        raise NotImplementedError

    def postorder(self) -> list[dict]:
        """Return postorder traversal of tree.

        Returns:
            List of {id, name} dicts in postorder (left, right, root)
        """
        # Replace this code with your implementation
        raise NotImplementedError


# Sample data for testing
if __name__ == "__main__":
    # Create a new tree
    tree = Tree()

    # Add sample student records
    # Format: tree.add(id, name)
    tree.add(50, "Alice")
    tree.add(30, "Bob")
    tree.add(70, "Charlie")
    tree.add(20, "Diana")
    tree.add(40, "Eve")
    tree.add(60, "Frank")
    tree.add(80, "Grace")

    print("Tree created with sample data:")
    print(f"Inorder traversal (sorted by ID): {tree.inorder()}")
    print(f"Preorder traversal: {tree.preorder()}")
    print(f"Postorder traversal: {tree.postorder()}")

    # Test find_node
    print("\nTesting find_node:")
    node = tree.find_node(30)
    if node:
        print(f"Find ID 30: Found node with id={node.id}, name={node.name}")
    else:
        print("Find ID 30: Not found")

    node = tree.find_node(999)
    if node:
        print(f"Find ID 999: Found node with id={node.id}, name={node.name}")
    else:
        print("Find ID 999: Not found")

    print("\nTest complete! Run 'python test_main.py' to run automated tests.")
