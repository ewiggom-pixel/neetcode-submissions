class Solution:
    
    from collections import Counter
    
    def minWindow(self, s: str, t: str) -> str:
        
        if not t or not s:
            return ""

        
        end = start = 0
        need = Counter(t)
        missing = len(t)
        L = 0
        
        
        for R, ch in enumerate(s, 1):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            if missing == 0:
                while need[s[L]] < 0:
                    need[s[L]] +=1
                    L +=1
                if end == 0 or R- L < end - start:
                    start, end = L, R


        return s[start:end]
