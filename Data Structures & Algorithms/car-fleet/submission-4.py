import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(list(zip(position,speed)))
        stack = []
        min_time = (target - pos_speed[-1][0])/pos_speed[-1][1]
        fleets = 1
        for p,s in reversed(pos_speed):
            time_needed = (target-p)/s
            if time_needed <= min_time:
                pass
                # min_time = time_needed
            else:
                min_time = time_needed
                fleets+=1
            print(p,s,time_needed,min_time,fleets)
        return fleets
