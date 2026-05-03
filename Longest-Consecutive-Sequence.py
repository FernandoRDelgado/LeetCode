1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        nums = sorted(nums)
4        max_length = 1
5        current_length = 1
6
7        if len(nums) == 0:
8            return 0
9
10        for i in range(1, len(nums)):
11            if nums[i - 1] == nums[i]:
12                continue
13            elif nums[i - 1] == nums [i] - 1:
14                current_length += 1
15                if current_length > max_length:
16                    max_length = current_length
17            else:
18                current_length = 1
19        
20        return max_length
21