1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stack = []
4        for token in tokens:
5            if token == "+":
6                stack.append(stack.pop() + stack.pop())
7            elif token == "-":
8                operand1, operand2 = stack.pop(), stack.pop()
9                stack.append(operand2 - operand1)
10            elif token == "*":
11                stack.append(stack.pop() * stack.pop())
12            elif token == "/":
13                operand1, operand2 = stack.pop(), stack.pop()
14                stack.append(math.trunc(operand2 / operand1))
15            else:
16                stack.append(int(token))
17        return stack[0]
18        