class Solution:
    def isHappy(self, n: int) -> bool:
        def sumofsqure(n):

            output = 0

            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10

            return output

        seen = set()

        while n != 1:
            
            n = sumofsqure(n)


            if n in seen:
                return False
            seen.add(n)

        return True


        


       