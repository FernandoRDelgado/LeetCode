1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        horizontal = defaultdict(int)
4        vertical = defaultdict(int)
5        box = defaultdict(int)
6
7        for i in range(len(board)):
8            for num in board[i]:
9                if num == ".":
10                    continue
11                else:
12                    horizontal[num] += 1
13            for tally in horizontal.values():
14                if tally > 1:
15                    return False
16            horizontal = defaultdict(int)
17        
18        for k in range(len(board)):
19            for j in range(len(board)):
20                for i in range(len(board)):
21                    if board[i][j] == ".":
22                        continue
23                    else:
24                        vertical[board[i][j]] += 1
25                for tally in vertical.values():
26                    if tally > 1:
27                        return False
28                vertical = defaultdict(int)
29
30        for k in range(0, 9, 3):
31            for l in range(0, 9, 3):
32                for i in range(3):
33                    for j in range(3):
34                        if board[i + k][j + l] == ".":
35                            continue
36                        else:
37                            box[board[i + k][j + l]] += 1
38                for tally in box.values():
39                    if tally > 1:
40                        return False
41                box = defaultdict(int)
42
43        return True
44        