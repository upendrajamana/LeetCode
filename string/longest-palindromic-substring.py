class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        res=""
        max_len=0
        for i in range(len(s)):
            #for odd length
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>max_len:
                    max_len=r-l+1
                    res=s[l:r+1]
                r+=1
                l-=1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>max_len:
                    max_len=r-l+1
                    res=s[l:r+1]
                r+=1
                l-=1
        return res
            