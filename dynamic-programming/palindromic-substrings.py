class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def countpalindrome(s,left,right):
            count=0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count+=1
                left-=1
                right+=1
            return count
        count=0
        for i in range(len(s)):
            count+=countpalindrome(s,i,i)
            count+=countpalindrome(s,i,i+1)
        
        return count
