import unittest


# their solution without space
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_binary_search_tree(root, lower_bound=-float('inf'), upper_bound=float('inf')):
    if not root:
        return True

    if root.value >= upper_bound or root.value <= lower_bound:
        return False

    left_is_valid = is_binary_search_tree(root.left, lower_bound, root.value)
    right_is_valid = is_binary_search_tree(root.right, root.value, upper_bound)

    return left_is_valid and right_is_valid


# my code with more space
# Time Complexity: O(n)
# Space Complexity: O(n**2)
def is_binary_search_tree(root):
    def dfs(node, values):
        if not node:
            return

        dfs(node.left, values)
        values.append(node.value)
        dfs(node.right, values)

    values = []
    dfs(root, values)

    for i in range(1, len(values)):
        if values[i - 1] > values[i]:
            return False
    return True


class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_valid_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_both_subtrees_valid(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(60)
        right.insert_left(70)
        right.insert_right(90)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_out_of_order_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(70)
        right_right = right.insert_right(60)
        right_right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_one_node_tree(self):
        tree = Test.BinaryTreeNode(50)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)
