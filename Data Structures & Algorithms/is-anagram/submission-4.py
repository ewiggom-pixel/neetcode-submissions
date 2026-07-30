class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        set1 = defaultdict(int)
        
        
        for char in s:
            set1[char] += 1
        for char in t:
            set1[char] -= 1
            if set1[char] < 0:
                return False
        return True
            
        