class Solution:
    def trap(self, height: List[int]) -> int:
        

        # so the water stored is equal to the max_height - index right.
        # when we see the new max height for each subsqeuent one we can add that much water to it minus the amount at that array. So bascially we walk from each side and track what the new max is so we give a count of all the water. 

        L = 0
        R = len(height) - 1
        count = 0
        maxLeft = height[L]
        maxRight = height[R]
        count = 0
        while L < R:
            if maxLeft < maxRight:
                L += 1
                maxLeft = max(maxLeft, height[L])
                count += maxLeft - height[L]
            else: 
                R -= 1
                maxRight = max(maxRight, height[R])
                count += maxRight - height[R]

        return count

