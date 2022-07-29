class Solution:
    def isPalindrome(self, s: str) -> bool:
        for c in s:
            if c.isalnum():
                s =''.join(c.lower())
            return s == s[::-1]
