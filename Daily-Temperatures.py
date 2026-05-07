1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        answer = [0 for x in temperatures]
4        next_biggest = dict()
5        for i in range(len(temperatures)):
6            for j in range(i + 1, len(temperatures)):
7                if temperatures[i] in next_biggest.keys():
8                    if next_biggest[temperatures[i]] > i:
9                        answer[i] = next_biggest[temperatures[i]] - i
10                        break
11                    if next_biggest[temperatures[i]] == -math.inf:
12                        break
13                if temperatures[i] < temperatures[j]:
14                    answer[i] = j - i
15                    next_biggest[temperatures[i]] = j
16                    break
17                if j == len(temperatures) - 1:
18                    next_biggest[temperatures[i]] = -math.inf
19        return answer