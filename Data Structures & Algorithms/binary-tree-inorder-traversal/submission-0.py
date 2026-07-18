class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        
        left = self.inorderTraversal(root.left)
        val = root.val
        right = self.inorderTraversal(root.right)

        return left + [val] + right