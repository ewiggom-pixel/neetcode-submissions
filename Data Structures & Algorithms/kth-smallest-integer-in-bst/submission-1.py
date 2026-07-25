class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int, state: list = None) -> int:
        
        #bst but we just run the recursive through the preorder then when K = count we have 
        # right number
    
        # Optimal is to do it with a stack which we are going to do now
        
        stack =[]
        curr = root

        while stack is not None or curr is not None:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right