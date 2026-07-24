import unittest
import main


class TestNodeClass(unittest.TestCase):
    """Unit tests for Node class."""

    def test_node_creation(self):
        """Check that node can be created with id and name."""
        try:
            node = main.Node(1, "Alice")
            self.assertEqual(node.id, 1, "Node ID should be set correctly")
            self.assertEqual(node.name, "Alice", "Node name should be set correctly")
            self.assertIsNone(node.left, "Node left should be None initially")
            self.assertIsNone(node.right, "Node right should be None initially")
        except NotImplementedError:
            self.skipTest("Node.__init__ not yet implemented")


class TestTreeAdd(unittest.TestCase):
    """Unit tests for Tree add operation."""

    def setUp(self):
        """Create a fresh tree for each test."""
        try:
            self.tree = main.Tree()
        except NotImplementedError:
            self.skipTest("Tree.__init__ not yet implemented")

    def test_add_to_empty_tree(self):
        """Check adding first node creates root."""
        try:
            self.tree.add(1, "Alice")
            self.assertIsNotNone(self.tree.root, "Root should be created after first add")
            self.assertEqual(self.tree.root.id, 1, "Root ID should be 1")
            self.assertEqual(self.tree.root.name, "Alice", "Root name should be Alice")
        except NotImplementedError:
            self.skipTest("Tree.add not yet implemented")

    def test_add_smaller_id(self):
        """Check adding smaller ID goes to left."""
        try:
            self.tree.add(50, "Alice")
            self.tree.add(30, "Bob")
            self.assertIsNotNone(self.tree.root.left, "Left child should be created")
            self.assertEqual(self.tree.root.left.id, 30, "Left child ID should be 30")
        except NotImplementedError:
            self.skipTest("Tree.add not yet implemented")

    def test_add_larger_id(self):
        """Check adding larger ID goes to right."""
        try:
            self.tree.add(50, "Alice")
            self.tree.add(70, "Bob")
            self.assertIsNotNone(self.tree.root.right, "Right child should be created")
            self.assertEqual(self.tree.root.right.id, 70, "Right child ID should be 70")
        except NotImplementedError:
            self.skipTest("Tree.add not yet implemented")

    def test_add_duplicate_id(self):
        """Check that duplicate ID is ignored."""
        try:
            self.tree.add(50, "Alice")
            self.tree.add(50, "Bob")  # Duplicate ID
            self.assertEqual(self.tree.root.name, "Alice", "Duplicate ID should not update name")
        except NotImplementedError:
            self.skipTest("Tree.add not yet implemented")

    def test_add_multiple_nodes(self):
        """Check adding multiple nodes creates correct structure."""
        try:
            self.tree.add(50, "Alice")
            self.tree.add(30, "Bob")
            self.tree.add(70, "Charlie")
            self.tree.add(20, "Diana")
            self.tree.add(40, "Eve")

            # Verify structure
            self.assertEqual(self.tree.root.id, 50)
            self.assertEqual(self.tree.root.left.id, 30)
            self.assertEqual(self.tree.root.right.id, 70)
            self.assertEqual(self.tree.root.left.left.id, 20)
            self.assertEqual(self.tree.root.left.right.id, 40)
        except NotImplementedError:
            self.skipTest("Tree.add not yet implemented")


class TestTreeFindNode(unittest.TestCase):
    """Unit tests for Tree find_node operation."""

    def setUp(self):
        """Create a tree with sample data for each test."""
        try:
            self.tree = main.Tree()
            self.tree.add(50, "Alice")
            self.tree.add(30, "Bob")
            self.tree.add(70, "Charlie")
            self.tree.add(20, "Diana")
            self.tree.add(40, "Eve")
        except NotImplementedError:
            self.skipTest("Tree setup not yet implemented")

    def test_find_root(self):
        """Check finding root node."""
        try:
            node = self.tree.find_node(50)
            self.assertIsNotNone(node, "Should find root node")
            self.assertEqual(node.id, 50, "Node ID should be 50")
            self.assertEqual(node.name, "Alice", "Node name should be Alice")
        except NotImplementedError:
            self.skipTest("Tree.find_node not yet implemented")

    def test_find_left_subtree(self):
        """Check finding node in left subtree."""
        try:
            node = self.tree.find_node(30)
            self.assertIsNotNone(node, "Should find node in left subtree")
            self.assertEqual(node.id, 30, "Node ID should be 30")
            self.assertEqual(node.name, "Bob", "Node name should be Bob")
        except NotImplementedError:
            self.skipTest("Tree.find_node not yet implemented")

    def test_find_right_subtree(self):
        """Check finding node in right subtree."""
        try:
            node = self.tree.find_node(70)
            self.assertIsNotNone(node, "Should find node in right subtree")
            self.assertEqual(node.id, 70, "Node ID should be 70")
            self.assertEqual(node.name, "Charlie", "Node name should be Charlie")
        except NotImplementedError:
            self.skipTest("Tree.find_node not yet implemented")

    def test_find_leaf_node(self):
        """Check finding leaf node."""
        try:
            node = self.tree.find_node(20)
            self.assertIsNotNone(node, "Should find leaf node")
            self.assertEqual(node.id, 20, "Node ID should be 20")
            self.assertEqual(node.name, "Diana", "Node name should be Diana")
        except NotImplementedError:
            self.skipTest("Tree.find_node not yet implemented")

    def test_find_non_existent(self):
        """Check finding non-existent ID returns None."""
        try:
            node = self.tree.find_node(999)
            self.assertIsNone(node, "Should return None for non-existent ID")
        except NotImplementedError:
            self.skipTest("Tree.find_node not yet implemented")

    def test_find_in_empty_tree(self):
        """Check finding in empty tree returns None."""
        try:
            empty_tree = main.Tree()
            node = empty_tree.find_node(1)
            self.assertIsNone(node, "Should return None for empty tree")
        except NotImplementedError:
            self.skipTest("Tree.find_node not yet implemented")


class TestTreeTraversal(unittest.TestCase):
    """Unit tests for Tree traversal operations."""

    def setUp(self):
        """Create a tree with sample data for each test."""
        try:
            self.tree = main.Tree()
            # Build tree:      50
            #                /    \
            #               30     70
            #              /  \   /  \
            #             20  40 60  80
            self.tree.add(50, "Alice")
            self.tree.add(30, "Bob")
            self.tree.add(70, "Charlie")
            self.tree.add(20, "Diana")
            self.tree.add(40, "Eve")
            self.tree.add(60, "Frank")
            self.tree.add(80, "Grace")
        except NotImplementedError:
            self.skipTest("Tree setup not yet implemented")

    def test_inorder_traversal(self):
        """Check inorder traversal returns sorted order."""
        try:
            result = self.tree.inorder()
            expected = [
                {"id": 20, "name": "Diana"},
                {"id": 30, "name": "Bob"},
                {"id": 40, "name": "Eve"},
                {"id": 50, "name": "Alice"},
                {"id": 60, "name": "Frank"},
                {"id": 70, "name": "Charlie"},
                {"id": 80, "name": "Grace"}
            ]
            self.assertEqual(result, expected, f"Inorder should return sorted order. Got: {result}")
        except NotImplementedError:
            self.skipTest("Tree.inorder not yet implemented")

    def test_preorder_traversal(self):
        """Check preorder traversal visits root before children."""
        try:
            result = self.tree.preorder()
            # Preorder: root, left subtree, right subtree
            # 50, 30, 20, 40, 70, 60, 80
            self.assertEqual(len(result), 7, "Should return all 7 nodes")
            self.assertEqual(result[0]["id"], 50, "First should be root")
            self.assertEqual(result[1]["id"], 30, "Second should be left child")
            self.assertEqual(result[2]["id"], 20, "Third should be left-left")
        except NotImplementedError:
            self.skipTest("Tree.preorder not yet implemented")

    def test_postorder_traversal(self):
        """Check postorder traversal visits children before root."""
        try:
            result = self.tree.postorder()
            # Postorder: left subtree, right subtree, root
            # 20, 40, 30, 60, 80, 70, 50
            self.assertEqual(len(result), 7, "Should return all 7 nodes")
            self.assertEqual(result[-1]["id"], 50, "Last should be root")
            self.assertEqual(result[0]["id"], 20, "First should be leftmost leaf")
        except NotImplementedError:
            self.skipTest("Tree.postorder not yet implemented")

    def test_traversal_empty_tree(self):
        """Check traversal on empty tree returns empty list."""
        try:
            empty_tree = main.Tree()
            self.assertEqual(empty_tree.inorder(), [], "Empty tree inorder should be []")
            self.assertEqual(empty_tree.preorder(), [], "Empty tree preorder should be []")
            self.assertEqual(empty_tree.postorder(), [], "Empty tree postorder should be []")
        except NotImplementedError:
            self.skipTest("Tree traversal not yet implemented")

    def test_traversal_single_node(self):
        """Check traversal on single node tree."""
        try:
            tree = main.Tree()
            tree.add(1, "Alice")

            inorder = tree.inorder()
            preorder = tree.preorder()
            postorder = tree.postorder()

            expected = [{"id": 1, "name": "Alice"}]
            self.assertEqual(inorder, expected)
            self.assertEqual(preorder, expected)
            self.assertEqual(postorder, expected)
        except NotImplementedError:
            self.skipTest("Tree traversal not yet implemented")


class TestNodeTraversal(unittest.TestCase):
    """Unit tests for Node traversal methods (recursive implementation)."""

    def setUp(self):
        """Create nodes for testing."""
        try:
            # Build small tree:      30
            #                       /  \
            #                      20   40
            self.root = main.Node(30, "Bob")
            self.root.left = main.Node(20, "Alice")
            self.root.right = main.Node(40, "Charlie")
        except NotImplementedError:
            self.skipTest("Node setup not yet implemented")

    def test_node_inorder(self):
        """Check node inorder traversal."""
        try:
            result = self.root.inorder()
            expected = [
                {"id": 20, "name": "Alice"},
                {"id": 30, "name": "Bob"},
                {"id": 40, "name": "Charlie"}
            ]
            self.assertEqual(result, expected, "Node inorder should traverse left-root-right")
        except NotImplementedError:
            self.skipTest("Node.inorder not yet implemented")

    def test_node_preorder(self):
        """Check node preorder traversal."""
        try:
            result = self.root.preorder()
            expected = [
                {"id": 30, "name": "Bob"},
                {"id": 20, "name": "Alice"},
                {"id": 40, "name": "Charlie"}
            ]
            self.assertEqual(result, expected, "Node preorder should traverse root-left-right")
        except NotImplementedError:
            self.skipTest("Node.preorder not yet implemented")

    def test_node_postorder(self):
        """Check node postorder traversal."""
        try:
            result = self.root.postorder()
            expected = [
                {"id": 20, "name": "Alice"},
                {"id": 40, "name": "Charlie"},
                {"id": 30, "name": "Bob"}
            ]
            self.assertEqual(result, expected, "Node postorder should traverse left-right-root")
        except NotImplementedError:
            self.skipTest("Node.postorder not yet implemented")

    def test_leaf_node_traversal(self):
        """Check traversal on leaf node."""
        try:
            leaf = main.Node(20, "Alice")
            expected = [{"id": 20, "name": "Alice"}]

            self.assertEqual(leaf.inorder(), expected)
            self.assertEqual(leaf.preorder(), expected)
            self.assertEqual(leaf.postorder(), expected)
        except NotImplementedError:
            self.skipTest("Node traversal not yet implemented")


if __name__ == '__main__':
    unittest.main()
