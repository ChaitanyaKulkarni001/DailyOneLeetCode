def checker(root, currentSum):
        if root is None:
            return False

        currentSum += root.val

        # Check if it's a leaf node
        if root.left is None and root.right is None:
            return currentSum == targetSum

        # Recursively check left and right subtrees
        return checker(root.left, currentSum) or checker(root.right, currentSum)

    return checker(root, 0)
