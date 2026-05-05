1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.min = math.inf
6        self.min_index = 0
7
8    def push(self, val: int) -> None:
9        if val or val == 0:
10            if val < self.min:
11                self.stack.append([val, self.min_index])
12                self.min = val
13                self.min_index = len(self.stack) - 1
14            else:
15                self.stack.append([val, self.min_index])
16
17    def pop(self) -> None:
18        if self.min_index == len(self.stack) - 1:
19            self.min_index = self.stack[-1][1]
20            self.min = self.stack[self.min_index][0]
21        self.stack.pop()
22
23    def top(self) -> int:
24        return self.stack[-1][0]
25
26    def getMin(self) -> int:
27        return self.stack[self.min_index][0]
28
29# Your MinStack object will be instantiated and called as such:
30# obj = MinStack()
31# obj.push(val)
32# obj.pop()
33# param_3 = obj.top()
34# param_4 = obj.getMin()