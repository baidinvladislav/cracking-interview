# my code with more space
# Time Complexity: O(n)
# Space Complexity: O(n)
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
