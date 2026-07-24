In this assignment, you should write your code in a **readable** way.

Your function definitions should have **appropriate docstrings**.

# Binary Search Tree for Student Records

## Sections Covered
1. Binary Search Trees
2. Tree Operations and Algorithms
3. Recursive Tree Traversal
4. Node Deletion (Reference Implementation)

## Binary Search Tree Basics

A **Binary Search Tree (BST)** is a data structure where each node has at most two children, and the tree is organised such that:
- All nodes in the left subtree have IDs less than the current node
- All nodes in the right subtree have IDs greater than the current node
- No duplicate IDs are allowed

This structure enables efficient searching, insertion, and deletion operations.

### Tree Structure Example
```
        50 (Alice)
       /    \
    30(Bob)  70(Charlie)
    /    \    /     \
20(Diana) 40(Eve) 60(Frank) 80(Grace)
```

## Part 1: Tree Operations

### Node Class

The `Node` class represents a single node in the tree with the following attributes:
- `id`: Student ID (integer, used as sorting key)
- `name`: Student name (string, data)
- `left`: Reference to left child node (or None)
- `right`: Reference to right child node (or None)

Implement the `Node` class.

### Tree Class

The `Tree` class manages the binary search tree with the following attributes:
- `root`: The root node - a `Node` instance, or `None` if the binary tree is empty.

**Methods to implement**
- `add(id, name) -> None`: Adds a new student record into the binary tree
- `find_node(id) -> Node | None`: Find student by ID and return the `Node` representing the student

## Part 2: Tree Traversal

Tree traversal involves visiting each node of the tree in a particular order.

- **Pre-order traversal:** Visit the root node first, then recursively traverse the left subtree, then recursively traverse the right subtree. (Root → Left → Right)
- **In-order traversal:** Recursively traverse the left subtree first, then visit the root node, then recursively traverse the right subtree. For a BST, this produces nodes in sorted order by ID. (Left → Root → Right)
- **Post-order traversal:** Recursively traverse the left subtree first, then recursively traverse the right subtree, then visit the root node. (Left → Right → Root) 

For this part of the exercise, we will use a recursive implementation that returns the traversal result as a list of dicts. Each dict represents student data in the following format:

```python
{
    "id": ...,
    "name": ...
}
```

Implement the following `Node` class methods:
- `preorder()` → list[dict]: Return student data from the node's subtree using preorder traversal (root, left, right)
- `inorder()` → list[dict]: Return student data from the node's subtree using inorder traversal (left, root, right)
- `postorder()` → list[dict]: Return student data from the node's subtree using postorder traversal (left, right, root)

Implement the following `Tree` class methods:
- `preorder()` → list[dict]: Calls `preorder()` on the root node if it is not empty, or an empty list if the tree is empty
- `inorder()` → list[dict]: Calls `inorder()` on the root node if it is not empty, or an empty list if the tree is empty
- `postorder()` → list[dict]: Calls `postorder()` on the root node if it is not empty, or an empty list if the tree is empty

## Part 3: Node Deletion

While the concept and algorithm for node deletion is in the 9569 syllabus, implementation of node deletion is not required in the syllabus. A sample implementation is provided here for reference. You may wish to attempt it yourself as further practice before looking.

- `delete(id) -> bool`: Unlinks the node with matching id from the tree, returning `True` if successful or `False` if unsuccessful

**Algorithm description:** Binary seach tree node deletion handles 3 separate cases:

### Deleting a leaf node (no child nodes)

To remove a leaf node, simply unlink it from its parent node (by setting parent's `left` or `right` attribute to `None`)

### Deleting a single-child node

To remove a single-child node, link its parent to its remaining child. This will cause the node to be unlinked from the tree.

### Deleting a two-child node

1. Find the adjacent node: this is the next-smaller or next-larger node of the node to be deleted.
2. Copy the adjacent node's data to the node to be deleted. This will **replace** the `id` and `name` attributes of the node to be deleted, but not its `left` and `right` attributes.
3. Remove the adjacent node. If the adjacent node has child nodes, this may result in a cascading (but finite) deletion of nodes.

### Sample implementation

```python
class Tree:
    # ... existing methods omitted for brevity
    def _find_with_parent(self, id: int) -> tuple[Node, Node, str] | None:
        """Helper function that returns the node with matching id, its
        parent, and whether it is the left or right child.
        If the node is not found, returns None.
        """
        parent = None
        node = self.root
        side = None
        while node is not None:
            if id == node.id:
                return node, parent, side
            elif id < node.id:
                if node.left is None:
                    return None
                else:
                    parent, node, side = node, node.left, "left"  # traverse left
            else:  # id > node.id
                if node.right is None:
                    return None
                else:
                    parent, node, side = node, node.right, "right"  # traverse right
        # if loop exits, node is not found
        return None

    def delete(self, id: int) -> bool:
        """Unlinks the node with matching id from the tree.
        Returns True if successful, False if unsuccessful.
        """
        # Handling of empty tree is not shown here for brevity
        # Use helper function to find matching node and its parent
        result = self._find_with_parent(id)
        if result is None:
            return False
        # Unpack for easier usage
        node, node_parent, side = result
        if node.left is None and node.right is None:
            delete_0_child_node(node_parent, node, side)
        elif node.left is None or node.right is None:
            delete_1_child_node(node_parent, node, side)
        else:
            delete_2_child_node(node_parent, node, side)

def delete_0_child_node(parent: Node, node: Node, side: str) -> None:
    """Delete a leaf node."""
    if side == "left":
        parent.left = None
    elif side == "right":
        parent.right = None

def delete_1_child_node(parent: Node, node: Node, side: str) -> None:
    """Delete a single-child node."""
    # Get a reference to node's child
    if node.left is not None:
        child = node.left
    elif node.right is not None:
        child = node.right
    # Unlink node
    if side == "left":
        parent.left = child
    elif side == "right":
        parent.right = child

def _get_adjacent_node(node: Node) -> tuple[Node, Node, str]:
    """Helper function that retrieves adjacent node of given node, along
    with its parent, and whether it is the left or right child.
    This implementation retrieves the next-larger node (smallest node of
    right subtree). You can also use the next-smaller node (largest node
    of left subtree).
    The node is assumed to have two child nodes, hence an adjacent node
    will exist.
    """
    parent = node
    node = node.right
    side = "right"
    while node.left is not None:
        parent = node
        node = node.left
        side = "left"
    return node, parent, side

def delete_2_child_node(parent: Node, node: Node, side: str) -> None:
    adjacent_node, adjacent_parent, adjacent_side = _get_adjacent_node(node)
    # Replace node data
    node.id, node.name = adjacent_node.id, adjacent_node.name
    # Remove adjacent_node
    if adjacent_node.left is None and adjacent_node.right is None:
        delete_0_child_node(adjacent_parent, adjacent_node, adjacent_side)
    elif adjacent_node.left is None or adjacent_node.right is None:
        delete_1_child_node(adjacent_parent, adjacent_node, adjacent_side)
    else:
        delete_2_child_node(adjacent_parent, adjacent_node, adjacent_side)
```

## Testing Instructions

1. **Manual Testing First**: Run `python main.py` to test with sample data
2. **Automated Tests**: Run `python test_main.py` to verify all operations

The tests will be skipped (not failed) for methods you haven't implemented yet, so you can test incrementally.

# Submission

Before submitting your code, run the automated tests on your functions. In the shell, type `python test_main.py` and press enter to see the results of the testing.
