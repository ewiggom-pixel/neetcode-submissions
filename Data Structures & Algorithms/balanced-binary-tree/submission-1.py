
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0

            return 1 + max(dfs(root.left), dfs(root.right))   
        
            

        if not root:
            return True
        
        if abs(dfs(root.left) - dfs(root.right)) > 1:
            return False

        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        return True