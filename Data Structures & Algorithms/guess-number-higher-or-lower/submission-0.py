# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        L = 1 
        H = n

        while L <= H:
            mid = (L+H) // 2
            result = guess(mid)

            if result > 0:
                L = mid + 1
            elif result < 0:
                H = mid - 1 
            else:
                return mid
        return 1