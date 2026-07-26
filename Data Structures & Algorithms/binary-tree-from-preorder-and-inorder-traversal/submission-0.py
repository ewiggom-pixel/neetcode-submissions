# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None

        
        root = preorder[0]

        split =  inorder.index(root)

        root = TreeNode(root)

        root.left = self.buildTree(preorder[1:1+split], inorder[:split])
        root.right = self.buildTree(preorder[1+split:], inorder[split+1:])

        return root