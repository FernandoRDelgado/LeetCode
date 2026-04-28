1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        num_set = set()
4        for digit in nums:
5            if digit in num_set:
6                return True
7            num_set.add(digit)
8        return False
9        