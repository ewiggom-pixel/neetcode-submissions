class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        result_len = 0

        for i, chr in enumerate(s):
            l = i
            r = i 
            #odd 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l) + 1 > result_len:
                    res = s[l:r+1]
                result_len = max(result_len, (r-l) + 1)
                
                r += 1
                l -= 1


            #even
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l) + 1 > result_len:
                    res = s[l:r+1]
                result_len = max(result_len, (r-l) + 1)
                
                r += 1
                l -= 1
        return res

