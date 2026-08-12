class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        memo = {}
        def dfs(i):
            if i == len(s):
                return [""]
            if i in memo:
                return memo[i]
            
            res = []
            for word in wordDict:
                if s[i: i+ len(word)] == word:
                    suffixes = dfs(i + len(word))
                    for suffix in suffixes:
                        res.append((word + " " + suffix).strip())
            
            memo[i] = res
            return res
        
        return dfs(0)