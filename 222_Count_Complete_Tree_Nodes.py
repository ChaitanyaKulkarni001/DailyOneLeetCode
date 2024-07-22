# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        count = 0
        def checker(root,count):
            if root is None: return count
            count +=1
            count = checker(root.left,count)
            # print(root.val)
            # print(root.val,count)
            
            count = checker(root.right,count)
            return count
            # print(left,right)\
            
        count = checker(root,count)
        return count
