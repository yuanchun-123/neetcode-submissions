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
                return (0, 0)
            #if rob node, cannot rob its children
            l_r, l_s = dfs(node.left)
            r_r, r_s = dfs(node.right)
            rob = node.val + l_s + r_s
            skip = max(l_r, l_s) + max(r_r, r_s)
            return [rob, skip]
        r, s = dfs(root)
        return max(r, s)
            