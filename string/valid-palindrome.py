class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        cleaned="".join(c for c in s if c.isalnum())
        return cleaned==cleaned[::-1]