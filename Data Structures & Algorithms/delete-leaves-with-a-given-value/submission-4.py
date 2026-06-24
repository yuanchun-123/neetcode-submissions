class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None
            
            # 1. Post-order: Process children first
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            # 2. Check if current node is now a leaf and matches target
            if not node.left and not node.right and node.val == target:
                return None
            
            # 3. FIX: You MUST return the node if it wasn't deleted
            return node

        # 4. FIX: Catch the return value to handle root deletion
        return dfs(root)