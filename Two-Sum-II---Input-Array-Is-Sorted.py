1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        low = 0
4        high = len(numbers) - 1
5        while low < high:
6            if numbers[low] + numbers[high] == target:
7                return [low + 1, high + 1]
8            elif numbers[low] + numbers[high] < target:
9                low += 1
10            else:
11                high -= 1