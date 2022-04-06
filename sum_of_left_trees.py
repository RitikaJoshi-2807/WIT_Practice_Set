# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result=[]
        def dfs(node, is_left):
            if not node:
                return None
        
            if (not node.left) and (not node.right) and is_left:
                result.append(node.val)
                
            dfs(node.left, is_left=True)
            dfs(node.right, is_left=False)
            
        dfs(root, False)
        return sum(result)
