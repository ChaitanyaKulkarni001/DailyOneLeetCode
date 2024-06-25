# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if ((p != None) and(q !=  None)):
            # print("inside",p.val,q.val)
            # return True
            if p.val!= q.val:
                # print("values")
                return False
            k = Solution().isSameTree(p.left,q.left)
            l =  Solution().isSameTree(p.right,q.right)
            if (k and l):
                return True
            return False
        elif( (p==None)and (q==None)):
            # print(False)
            return True
        else:
            return False
