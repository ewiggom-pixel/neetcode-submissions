class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        perms = [[]]
        for n in nums:
            nexPerm = []
            for p in perms:
                for i in range(len(p) + 1):
                    copy = p.copy()
                    copy.insert(i,n)
                    if copy not in nexPerm:
                        nexPerm.append(copy)
            perms = nexPerm
        return perms