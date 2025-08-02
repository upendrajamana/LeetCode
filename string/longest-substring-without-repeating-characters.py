class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        max_length=0
        charset=set()
        i=0
        count=0
        for j in range(len(s)):
            if s[j] not in charset:
                charset.add(s[j])
                max_length=max(max_length,j-i+1)
            else:
                while s[j] in charset:
                    charset.remove(s[i])
                    i+=1
                charset.add(s[j])

        return max_length
                


                