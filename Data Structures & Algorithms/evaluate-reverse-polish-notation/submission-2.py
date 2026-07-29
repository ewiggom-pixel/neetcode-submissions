class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []


        for tok in tokens:
                if tok == "+":
                    stack.append(int(stack.pop()) + int(stack.pop()))
                elif tok == "-":
                    right = int(stack.pop())
                    left = int(stack.pop())
                    stack.append(left - right)
                elif tok == "*":
                    stack.append(int(stack.pop()) * int(stack.pop()))
                elif tok == "/":
                    right = int(stack.pop())
                    left = int(stack.pop())
                    stack.append(int(left / right))
                else:
                    stack.append(tok)
        return int(stack.pop())