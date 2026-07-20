class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        L = 0

        R = len(numbers) -1
        results = []
        while L < R:
            stuff = numbers[L] + numbers[R]
            print(f" {stuff} stuff")
            if stuff < target:
                L += 1
                print(f"{L} L")
            if stuff > target:
                R -= 1
                print(f"{R} R")
            if stuff == target:
                results.append(L+1)
                results.append(R+1)
                return results