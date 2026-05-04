1class Solution:
2    def isValid(self, s: str) -> bool:
3        closure = {")", "]", "}"}
4        closed = []
5        opened = 0
6        for char in s:
7            if char == "(":
8                closed.append(")")
9                opened += 1
10            elif char == "{":
11                closed.append("}")
12                opened += 1
13            elif char == "[":
14                closed.append("]")
15                opened += 1
16            elif char in closure:
17                if len(closed) > 0 and char == closed[-1]:
18                    closed.pop()
19                    opened -= 1
20                else:
21                    return False
22        if opened == 0:
23            return True
24        else:
25            return False
26