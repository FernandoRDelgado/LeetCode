1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5
6    def push(self, val: int) -> None:
7        if self.stack:
8            self.stack.append((val, min(val, self.stack[-1][1])))
9        else:
10            self.stack.append((val, val))
11
12    def pop(self) -> None:
13        self.stack.pop()
14
15    def top(self) -> int:
16        return self.stack[-1][0]
17
18    def getMin(self) -> int:
19        return self.stack[-1][1]
20
21# Your MinStack object will be instantiated and called as such:
22# obj = MinStack()
23# obj.push(val)
24# obj.pop()
25# param_3 = obj.top()
26# param_4 = obj.getMin()