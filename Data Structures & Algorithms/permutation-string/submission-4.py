class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0

        checker = defaultdict(int)

        for char in s1:
            checker[char] += 1
        


        for char in s2:
            checker[char] -= 1
            while checker[char] < 0:
                checker[s2[l]] += 1 
                l += 1
            if (r - l + 1) == len(s1):
                return True
            r += 1
        return False