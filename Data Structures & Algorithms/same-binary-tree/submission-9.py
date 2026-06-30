# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        l, r = [], []
        def dfs(root, ls):
            if not root:
                ls.append("null")
                return
            ls.append(root.val)
            dfs(root.left, ls)
            dfs(root.right, ls)
        dfs(p, l)
        dfs(q, r)
        return l == r
