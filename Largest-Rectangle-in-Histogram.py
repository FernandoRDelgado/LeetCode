1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        largest = 0
4        stack = [-1]
5        
6        for i in range(len(heights)):
7            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
8                current_height = heights[stack.pop()]
9                current_width = i - stack[-1] - 1
10                if current_height * current_width > largest:
11                    largest = current_height * current_width
12            stack.append(i)
13
14        while stack[-1] != -1:
15            current_height = heights[stack.pop()]
16            current_width = len(heights) - stack[-1] - 1
17            if current_height * current_width > largest:
18                largest = current_height * current_width
19
20        return largest
21