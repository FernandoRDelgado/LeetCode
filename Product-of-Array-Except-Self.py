1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        prefix = dict()
4        suffix = dict()
5        prefix[0] = 1
6        suffix[len(nums) - 1] = 1
7        for i in range(1, len(nums)):
8            prefix[i] = prefix[i - 1] * nums[i - 1]
9            suffix[len(nums) - 1 - i] = suffix[len(nums) - i] * nums[len(nums) - i]
10
11        answer = []
12        for i in range(len(nums)):
13            answer.append(prefix[i] * suffix[i])
14        return answer
15        