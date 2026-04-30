1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        result = []
4        tally = dict()
5        processed = set()
6
7        for entry in nums:
8            if entry in processed:
9                tally[entry] += 1
10            else:
11                tally[entry] = 1
12                processed.add(entry)
13
14        sorted_tally = {k: v for k, v in sorted(tally.items(), key=lambda item: item[1])}
15
16        for i in range(k):
17            result.append(list(sorted_tally.keys())[-1 - i])
18
19        return result
20        