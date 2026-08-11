class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        L = 0
        R = 0


        if not t:
            return 0
        
        if not s:
            return 0
        
        while L < len(s) and R < len(t):

            if s[L] == t[R]:
                R += 1

            L += 1
        
        return len(t) - len(t[:R])