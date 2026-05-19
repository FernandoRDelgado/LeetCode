1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums = sorted(nums)
4        output = []
5        for i in range(len(nums)):
6            if nums[i] > 0:
7                break
8            if i == 0 or nums[i] != nums[i - 1]:    
9                lower = i + 1
10                upper = len(nums) - 1
11                while lower < upper:
12                    if nums[i] + nums[lower] + nums[upper] > 0:
13                        upper -= 1
14                    elif nums[i] + nums[lower] + nums[upper] < 0:
15                        lower += 1
16                    else:
17                        output.append([nums[i], nums[lower], nums[upper]])
18                        lower += 1
19                        upper -= 1
20                        while lower < upper and nums[lower] == nums[lower - 1]:
21                            lower += 1
22        return output
23