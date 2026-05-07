1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        answer = [0 for x in temperatures]
4        next_biggest = defaultdict(int)
5        for i in range(len(temperatures)):
6            for j in range(i + 1, len(temperatures)):
7                if next_biggest[temperatures[i]] == -math.inf:
8                    break
9                if next_biggest[temperatures[i]] > i:
10                    answer[i] = next_biggest[temperatures[i]] - i
11                    break
12                if temperatures[i] < temperatures[j]:
13                    answer[i] = j - i
14                    next_biggest[temperatures[i]] = j
15                    break
16                if j == len(temperatures) - 1:
17                    next_biggest[temperatures[i]] = -math.inf
18        return answer