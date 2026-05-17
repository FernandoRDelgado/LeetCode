1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        explored = set()
4        for i in range(len(numbers)):
5            if numbers[i] in explored:
6                continue
7            explored.add(numbers[i])
8            complement = target - numbers[i]
9            for j in range(i + 1, len(numbers)):
10                if numbers[j] == complement:
11                    return [i + 1, j + 1]