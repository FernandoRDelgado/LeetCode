1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        nums = set(nums)
4        max_length = 1
5        current_length = 1
6
7        if len(nums) == 0:
8            return 0
9
10        for num in nums:
11            if num - 1 in nums:
12                continue
13            while num + 1 in nums:
14                current_length += 1
15                if current_length > max_length:
16                    max_length = current_length
17                num += 1
18            else:
19                current_length = 1
20        
21        return max_length
22