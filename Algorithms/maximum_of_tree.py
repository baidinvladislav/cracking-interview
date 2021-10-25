# Python3 program to find maximum
# and minimum in a Binary Tree

# A class to create a new node


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Returns maximum value in a
# given Binary Tree


def findMax(root):
    # Base case
    if (root == None):
        return float('-inf')

    # Return maximum of 3 values:
    # 1) Root's data 2) Max in Left Subtree
    # 3) Max in right subtree
    res = root.data
    lres = findMax(root.left)
    rres = findMax(root.right)
    if lres > res:
        res = lres
    if rres > res:
        res = rres
    return res


# Driver Code
if __name__ == '__main__':
    root = newNode(2)
    root.left = newNode(7)
    root.right = newNode(5)
    root.left.right = newNode(6)
    root.left.right.left = newNode(1)
    root.left.right.right = newNode(11)
    root.right.right = newNode(9)
    root.right.right.left = newNode(4)

    # Function call
    print("Maximum element is", findMax(root))
