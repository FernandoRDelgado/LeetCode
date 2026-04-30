1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        tally = defaultdict(int)
4
5        for entry in nums:
6            tally[entry] += 1
7
8        sorted_tally = {k: v for k, v in sorted(tally.items(), key=lambda item: item[1])}
9
10        result = []
11        for i in range(k):
12            result.append(list(sorted_tally.keys())[-1 - i])
13
14        return result
15        