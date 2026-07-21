class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "":
            return len(s)
        length = 0
        L = 0
        R = L 
        things_seen = set()
        for R in range(len(s)):
            while s[R] in things_seen:
                things_seen.remove(s[L])
                L += 1
                
                
                
                # print(s[R])
            things_seen.add(s[R])
            length = max(length, len(things_seen))
                
            # print(things_seen)
        
                

        
        length = max(length, len(things_seen))
        
        
        return length