class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # recursively invert left and right subtrees
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # swap the subtrees
        root.left = right
        root.right = left

        return root