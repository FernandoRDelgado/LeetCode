1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        running_total = 0
4        i = 0
5        if(len(tokens)) == 1:
6            return int(tokens[0])
7        while(len(tokens) > 1):
8            try:
9                operand = int(tokens[i])
10                i += 1
11                continue
12            except ValueError:
13                operator = tokens[i]
14                if operator == "+":
15                    running_total = int(tokens[i - 2]) + int(tokens[i - 1])
16                elif operator == "-":
17                    running_total = int(tokens[i - 2]) - int(tokens[i - 1])
18                elif operator == "*":
19                    running_total = int(tokens[i - 2]) * int(tokens[i - 1])
20                elif operator == "/":
21                    if abs(int(tokens[i - 1])) > abs(int(tokens[i - 2])):
22                        running_total = 0
23                    else:
24                        running_total = math.trunc(int(tokens[i - 2]) / int(tokens[i - 1]))
25                tokens.pop(i)
26                tokens.pop(i - 1)
27                tokens.pop(i - 2)
28                tokens.insert(i - 2, running_total)
29                i = 0
30        return running_total
31        