1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        indices = dict()
4        for i in range(len(nums)):
5            complement = target - nums[i]
6            if complement in indices.keys():
7                return [i, indices[complement]]
8            indices[nums[i]] = i
9        return []
10        