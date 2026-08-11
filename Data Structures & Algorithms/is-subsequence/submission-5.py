class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        L, R = 0, 0

        if not s:
            return True 
        
        while L < len(t):
            if s[R] == t[L]:
                R += 1
            if R == len(s):
                return True

            
            L += 1
        
            
        return False
                