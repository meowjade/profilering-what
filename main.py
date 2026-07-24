class Node:
    """Node class for binary tree storing student records."""

    def __init__(self, id: int, name: str):
        """Initialize a new node with student record.

        Args:
            id: Student ID (used as sorting key)
            name: Student name
        """
        # Replace this code with your implementation
        self.id: int = id
        self.name: str = name
        self.left: Node | None = None
        self.right: Node | None = None

    def preorder(self) -> list[dict]:
        """Return preorder traversal as list of dicts.

        Returns:
            List of {id, name} dicts in preorder (root, left, right)
        """
        res: list[dict] = []
        res.append({"id": self.id, "name": self.name})
        if self.left is not None:
            res += self.left.preorder()
        if self.right is not None:
            res += self.right.preorder()
        return res

    def inorder(self) -> list[dict]:
        """Return inorder traversal as list of dicts.

        Returns:
            List of {id, name} dicts in inorder (left, root, right)
        """
        res: list[dict] = []
        if self.left is not None:
           res += self.left.inorder()
        res.append({"id": self.id, "name": self.name})
        if self.right is not None:
            res += self.right.inorder()
        return res

    def postorder(self) -> list[dict]:
        """Return postorder traversal as list of dicts.

        Returns:
            List of {id, name} dicts in postorder (left, right, root)
        """
        res: list[dict] = []
        if self.left is not None:
            res += self.left.postorder()
        if self.right is not None:
            res += self.right.postorder()
        res.append({"id": self.id, "name": self.name})
        return res



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
        if self.root is None:
            self.root = Node(id, name)

        current = self.root
        while True:
            if current.id > id:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = Node(id, name)
                    break
            elif current.id < id:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = Node(id, name)
                    break
            else:
                break

    def find_node(self, id: int) -> Node | None:
        """Find a student node by ID.

        Args:
            id: Student ID to search for

        Returns:
            Node object if found, None otherwise
        """
        current = self.root
        while current is not None:
            if current.id > id:
                current = current.left
            elif current.id < id:
                current = current.right
            else:
                break
        return current

    def delete(self, id: int) -> None:
        """Delete a student node by ID."""
        found_parent = self.root
        found = self.root
        while found is not None:
            if found.id > id:
                found_parent = found
                found = found.left
            elif found.id < id:
                found_parent = found
                found = found.right
            else:
                break

        if found is None:
            return
        # if only 1 child
        if found.left is None != found.right is None:
            if found.left is not None:
                replace = found.left
            elif found.right is not None:
                replace = found.right
            else:
                return
            found.id = replace.id
            found.name = replace.name
            found.left = replace.left
            found.right = replace.right
            return
        # if 2 children
        if found.left is not None and found.right is not None:
            min = found.right.inorder()[0]
            self.delete(min["id"])
            found.id = min["id"]
            found.name = min["name"]
            return
        # found has no children, just nuke the Node
        if found_parent is not None:
            if found_parent.left == found:
                found_parent.left = None
            else:
                found_parent.right = None

    def preorder(self) -> list[dict]:
        """Return preorder traversal of tree.

        Returns:
            List of {id, name} dicts in preorder (root, left, right)
        """
        if self.root is None:
            return []
        return self.root.preorder()

    def inorder(self) -> list[dict]:
        """Return inorder traversal of tree.

        Returns:
            List of {id, name} dicts in inorder (left, root, right)
        """
        if self.root is None:
            return []
        return self.root.inorder()

    def postorder(self) -> list[dict]:
        """Return postorder traversal of tree.

        Returns:
            List of {id, name} dicts in postorder (left, right, root)
        """
        if self.root is None:
            return []
        return self.root.postorder()


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

    t2 = Tree()
    t2.add(50, "a")
    t2.add(40, "b")
    t2.add(70, "c")
    t2.add(60, "d")
    t2.add(80, "e")
    print(t2.preorder())
    t2.delete(50)
    print(t2.preorder())

    print("\nTest complete! Run 'python test_main.py' to run automated tests.")
