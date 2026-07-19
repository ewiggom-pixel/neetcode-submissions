# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        count= 0

        def dfs(root, count, targetSum):
            if not root:
                return False
            count += root.val
            if not root.left and not root.right and count ==targetSum:
                return True
            if dfs(root.left, count, targetSum):
                return True
            if dfs(root.right, count, targetSum):
                return True
            return False

        return dfs(root, 0, targetSum)