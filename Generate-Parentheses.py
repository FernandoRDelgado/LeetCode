1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        output = []
4
5        def backtracking(current_string, opened_count, closed_count):
6            if len(current_string) == 2 * n:
7                output.append(current_string)
8                return
9            
10            if opened_count < n:
11                current_string += "("
12                backtracking(current_string, opened_count + 1, closed_count)
13                current_string = current_string[:-1]
14            
15            if closed_count < opened_count:
16                current_string += ")"
17                backtracking(current_string, opened_count, closed_count + 1)
18                current_string = current_string[:-1]
19        
20        backtracking("", 0, 0)
21        
22        return output
23