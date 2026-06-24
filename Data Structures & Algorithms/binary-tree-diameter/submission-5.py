class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 
        
        def dfs(node):
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            # Update the class variable, not a local one
            self.res = max(self.res, l + r)
            
            # Still return height to the parent
            return max(l, r) + 1
            
        dfs(root)
        return self.res