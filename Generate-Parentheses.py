1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        output = []
4
5        def isValid(string):
6            opened = 0
7            if len(string) == 0:
8                return True
9            if string[0] == ")":
10                return False
11            for char in string:
12                if char == "(":
13                    opened += 1
14                else:
15                    opened -= 1
16                if opened < 0:
17                    return False
18            return opened == 0
19        
20        q = deque([""])
21        while q:
22            current_string = q.popleft()
23            if len(current_string) == 2 * n:
24                if isValid(current_string):
25                    output.append(current_string)
26                continue
27            q.append(current_string + ")")
28            q.append(current_string + "(")
29        
30        return output
31
32            
33