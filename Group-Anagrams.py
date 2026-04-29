1class Solution:
2    from collections import defaultdict
3
4    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
5        
6        tally = dict(defaultdict(int))
7        
8        for i in range(len(strs)):
9            tally[strs[i]] = defaultdict(int)
10            if len(strs[i]) == 0:
11                tally[strs[i]][""] = 1
12            for char in strs[i]:
13                if char in tally[strs[i]].keys():
14                    tally[strs[i]][char] += 1
15                else:
16                    tally[strs[i]][char] = 1
17
18        output = []
19        processed = defaultdict(bool)
20
21        for i in range(len(strs)):
22            anagrams = []
23            if processed[i]:
24                continue
25            if not processed[i]:
26                anagrams.append(strs[i])
27            processed[i] = True
28            for j in range(len(strs)):
29                matched = False
30                if len(strs[i]) != len(strs[j]) or processed[j]:
31                    continue
32                for key in tally[strs[i]].keys():
33                    if tally[strs[i]][key] == tally[strs[j]][key]:
34                        matched = True
35                    else:
36                        matched = False
37                        break
38                if matched:
39                    if not processed[j]:
40                        anagrams.append(strs[j])
41                        processed[j] = True
42            if len(anagrams) > 0:
43                output.append(anagrams.copy())
44        
45        return output
46
47        