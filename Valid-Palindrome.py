1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        converted =  ""
4        for char in s:
5            if char.isalnum():
6                converted += char.lower()
7        return converted == converted[::-1]
8        