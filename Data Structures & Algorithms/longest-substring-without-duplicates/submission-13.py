class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        if s == "":
            return len(s)
        length = 0
        L = 0
        R = L 
        things_seen = {}
        for R, ch in enumerate(s):
            if ch in things_seen and things_seen[ch] >= L:
                L = things_seen[ch] + 1
            things_seen[ch] = R

            if R - L + 1 > best:
                best = R -L + 1
        return best
            
                