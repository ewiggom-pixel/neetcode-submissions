class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "":
            return len(s)
        length = 0
        L = 0
        R = L 
        things_seen = set()
        while R < len(s):
            if s[R] in things_seen:
                length = max(length, len(things_seen))
                #things_seen.remove(s[R])
                #length = (max)  
                things_seen.clear()
                L += 1
                R = L
                
                
                # print(s[R])
            things_seen.add(s[R])
            R += 1
            # print(things_seen)
        
                

        
        length = max(length, len(things_seen))
        
        
        return length