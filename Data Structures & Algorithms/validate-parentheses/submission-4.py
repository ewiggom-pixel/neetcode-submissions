class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = []
        
        
        
        
        for chr in s:
            if chr == "(" or chr == "{" or chr == "[":
                stack1.append(chr)
            elif chr == "]" and stack1 and stack1[-1] == "[":
                stack1.pop()
            elif chr == "}" and stack1 and stack1[-1] == "{" :
                stack1.pop()
            elif chr == ")" and stack1 and stack1[-1] == "(" :
                stack1.pop()
            else:
                return False 
        return len(stack1) == 0
            