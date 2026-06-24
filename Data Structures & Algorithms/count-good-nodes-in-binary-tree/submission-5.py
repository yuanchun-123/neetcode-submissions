# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        
        def dfs(node, m):
            if not node:
                return 0
            if node.val >= m:
                self.res += 1
            m = max(m, node.val)
            dfs(node.left, m)
            dfs(node.right, m)
        dfs(root, root.val)
        return self.res
            
