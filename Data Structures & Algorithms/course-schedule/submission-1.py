class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        manp = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            manp[course].append(prereq)
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if manp[crs] == []:
                return True

            visited.add(crs)
            for prereq in manp[crs]:
                if not dfs(prereq):
                    return False
            visited.remove(crs)
            manp[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True