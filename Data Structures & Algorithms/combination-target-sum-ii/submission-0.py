class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combs = []
        self.helper(0, [], combs, candidates, target)
        return combs

    def helper(self, i, curComb, combs, candidates, target):
        current_sum = sum(curComb)
        if current_sum == target:
            combs.append(curComb.copy())
            return
        if i >= len(candidates) or current_sum > target:
            return

        #pick to add
        curComb.append(candidates[i])
        self.helper(i + 1, curComb, combs, candidates, target)
        curComb.pop()
    
        # pick to not add
        while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1
        self.helper(i + 1, curComb, combs, candidates, target)