class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digits_list = {
            
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",

        }
        def backtrack(n, curStr): 

            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digits_list[digits[n]]:
                backtrack(n+1,curStr + c)

        backtrack(0,"")

        return res
            
            
        
