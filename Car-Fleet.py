1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        fleets = len(position)
4        cars = sorted(zip(position, speed))
5        hours_to_target = [float(target - position) / speed for position, speed in cars]
6        
7        while len(hours_to_target) > 1:
8            lead = hours_to_target.pop()
9            if lead >= hours_to_target[-1]:
10                hours_to_target[-1] = lead
11                fleets -= 1
12
13        return fleets
14