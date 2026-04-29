1from collections import defaultdict
2
3class Solution:
4    def isAnagram(self, s: str, t: str) -> bool:
5        source = defaultdict(int)
6        contestant = defaultdict(int)
7        for char in s:
8            if char in source.keys():
9                source[char] += 1
10            else:
11                source[char] = 1
12        for char in t:
13            if char in contestant.keys():
14                contestant[char] += 1
15            else:
16                contestant[char] = 1
17        if len(source) != len(contestant):
18            return False
19        for key in source.keys():
20            if source[key] == contestant[key]:
21                continue
22            else:
23                return False
24        return True
25
26
27        