1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        horizontal = set()
4        vertical = set()
5        box = set()
6
7        for i in range(len(board)):
8            for num in board[i]:
9                if num == ".":
10                    continue
11                else:
12                    if num in horizontal:
13                        return False
14                    else:
15                        horizontal.add(num)
16            horizontal = set()
17        
18        for j in range(len(board)):
19            for i in range(len(board)):
20                if board[i][j] == ".":
21                    continue
22                else:
23                    if board[i][j] in vertical:
24                        return False
25                    else:
26                        vertical.add(board[i][j])
27            vertical = set()
28
29        for k in range(0, len(board), len(board) // 3):
30            for l in range(0, len(board), len(board) // 3):
31                for i in range(len(board) // 3):
32                    for j in range(len(board) // 3):
33                        if board[i + k][j + l] == ".":
34                            continue
35                        else:
36                            if board[i + k][j + l] in box:
37                                return False
38                            else:
39                                box.add(board[i + k][j + l])
40                box = set()
41
42        return True
43        