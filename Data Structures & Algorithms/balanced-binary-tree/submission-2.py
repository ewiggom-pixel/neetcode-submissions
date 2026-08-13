class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(node):
            if not node:
                return 0
            
            left_h = checkHeight(node.left)
            if left_h == -1: return -1
            
            right_h = checkHeight(node.right)
            if right_h == -1: return -1
            
            if abs(left_h - right_h) > 1:
                return -1
            
            return max(left_h, right_h) + 1
            
        return checkHeight(root) != -1