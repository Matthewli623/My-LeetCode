# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        d1={}
        self.helper(root,1,d1)
        
        ans = float("-inf")
        tempmax = float("-inf")
        for key,val in d1.items():
            if tempmax<val:
                tempmax=val
                ans=key
        return ans
    
    def helper(self,r,level,l1):
        if not r:
            return None
        if level not in l1:
            l1[level]=r.val
        else:
            l1[level]+=r.val
        self.helper(r.right,level+1,l1)
        self.helper(r.left,level+1,l1)