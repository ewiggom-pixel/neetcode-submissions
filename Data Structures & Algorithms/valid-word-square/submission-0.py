class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        r = len(words)

        for i in range(r):
            for j in range(len(words[i])):
                if j >= r or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True