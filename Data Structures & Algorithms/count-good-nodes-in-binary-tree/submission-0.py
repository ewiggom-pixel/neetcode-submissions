# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        global_max = float("-inf")

        def dfs(root, global_max):

           
            if not root:
                return 0

            global_max = max(global_max, root.val)

            if root.val >= global_max:
                res = 1 
            else:
                res = 0
            
            res += dfs(root.left, global_max)
            res += dfs(root.right, global_max)
            return res

        return dfs(root,global_max)
