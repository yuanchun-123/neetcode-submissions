# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return [0, 0]
            lw, lwo = dfs(node.left)
            rw, rwo = dfs(node.right)
            withNode = node.val + lwo + rwo
            withoutNode = max(lw,lwo) + max(rw,rwo)
            return [withNode, withoutNode]
        w, wo = dfs(root)
        return max(w,wo)
            
            


