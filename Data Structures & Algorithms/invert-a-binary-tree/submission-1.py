class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root == None:
            return None
        
        queue = deque([root])

        while len(queue) > 0:
            for i in range(len(queue)):
                    curr = queue.popleft()
                    curr.left, curr.right = curr.right, curr.left
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
        return root