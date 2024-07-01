# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        # rootVal = root.val
        values = []
        def read_binary_tree(root):
            if root is None:
                # values.append(None)
                return 
            read_binary_tree(root.left)
            values.append(root.val)
            read_binary_tree(root.right)
        read_binary_tree(root)
        # print(values)
        n=len(values)
        diff = 10**20
        for i in range(n-1):
            for j in range(i+1, n):
                if abs(values[i]-values[j]) < diff:
                    diff = abs(values[i] - values[j])
    
        # Return min diff
        return diff
