class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #when I see this I think we walk through each letter and check if it in the dictionary, then once we hit a word we move the pointer to the R pointer and start again.

        # so this the right idea it just that we can do it recursively which means we can use memoization to make it so that it linear 
        #I do think there will be some edge case issue but this does not use dynamic programming at all so now i am confused.
        memo = {len(s) : True}
    
        def dfs(i):

            if i in memo:
                return memo[i]
            
            for word in wordDict:
                if s[i: i+len(word)] == word:
                    if dfs(i + len(word)):
                        memo[i] = False
                        return True
            memo[i] = False
            return False

        return dfs(0)
           
