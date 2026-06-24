class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node):
            if not node:
                return 0
            return max(dfs(node.left), dfs(node.right)) + 1

        return dfs(root)
        
