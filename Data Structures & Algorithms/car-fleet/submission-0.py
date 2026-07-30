class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        combined = list(zip(position, speed))
        the_answer = sorted(combined, reverse=True)

        fleets = 1
        prevTime = (target - the_answer[0][0]) / the_answer[0][1]

        for i in range(1 , len(the_answer)):
            curr = the_answer[i]
            currTime = (target - curr[0]) / curr[1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        return fleets
            