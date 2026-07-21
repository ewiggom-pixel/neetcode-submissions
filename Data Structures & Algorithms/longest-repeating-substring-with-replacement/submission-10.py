class Solution:
    def characterReplacement(self, S: str, k: int) -> int:
        length = 0
        set_s = set(S)
        for char in set_s:
            replace = 0
            L = 0
            for R in range(len(S)):
                if S[R] != char:
                    replace += 1
                
                while replace > k:
                    if S[L] != char:
                        replace -= 1
                    L += 1
                
                length = max(length, (R-L) + 1)
        return length