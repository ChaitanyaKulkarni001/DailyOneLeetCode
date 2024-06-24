Solution().# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # count = 1
        l =Solution().maxDepth(root.left)
        m = Solution().maxDepth(root.right)
        if l>m:
            return l+1
        return m+1
