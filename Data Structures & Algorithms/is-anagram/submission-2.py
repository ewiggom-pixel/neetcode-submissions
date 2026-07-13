class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_1 = sorted(t)
        set_2 = sorted(s)

        if set_1 == set_2:
            return True
        else:
            return False
        