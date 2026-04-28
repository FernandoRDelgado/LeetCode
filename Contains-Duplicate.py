1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        num_set = set(nums)
4        if len(nums) > len(num_set):
5                return True
6        else:
7            return False
8        