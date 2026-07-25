class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int, state: list = None) -> int:
        
        #bst but we just run the recursive through the preorder then when K = count we have 
        # right number
        
        if state == None:
            state = [0, None]


        if not root or state[1] is not None:
            return state[1]
        
        self.kthSmallest(root.left, k, state)

        if state[1] is not None:
            return state[1]

        state[0] += 1

        if state[0] == k:
            state[1] = root.val
            return state[1] 
        
        self.kthSmallest(root.right, k, state)

        return state[1]