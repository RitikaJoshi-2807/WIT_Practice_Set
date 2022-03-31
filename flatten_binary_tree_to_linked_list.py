# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        res = [root]
        while res:
            curr = res.pop()
            
            if curr.right:
                res.append(curr.right)
            if curr.left:
                res.append(curr.left)   
            if res:
                curr.right = res[-1]
            
            curr.left = None
