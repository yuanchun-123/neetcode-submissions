# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(node, l, r):
            if not node:
                return
            if not (l < node.val < r):
                self.res = False
                return
            dfs(node.left, l, node.val)
            dfs(node.right, node.val, r)
        dfs(root, -float('inf'), float('inf'))
        return self.res

