class Solution:
    def climbStairs(self, n: int, cache=None) -> int:
        if n <= 2:
            return n

        array = [0] * (n+ 1)

        array[1] = 1
        array[2] = 2

        for i in range(3,n + 1):
            array[i] = array[i-1] + array[i-2]
        
        return array[n]
