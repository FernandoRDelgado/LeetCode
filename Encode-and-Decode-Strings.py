1class Codec:
2    def encode(self, strs: List[str]) -> str:
3        """Encodes a list of strings to a single string.
4        """
5        coded = ""
6        for i in range(len(strs)):
7            if i < len(strs) - 1:
8                coded = coded + strs[i] + "\n"
9            else:
10                coded = coded + strs[i]
11        return coded
12        
13
14    def decode(self, s: str) -> List[str]:
15        """Decodes a single string to a list of strings.
16        """
17        print(s)
18        decoded = s.split('\n')
19        return decoded
20
21# Your Codec object will be instantiated and called as such:
22# codec = Codec()
23# codec.decode(codec.encode(strs))