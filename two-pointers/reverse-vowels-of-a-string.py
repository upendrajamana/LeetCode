class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels=set("aeiouAEIOU")
        left=0
        right=len(s)-1
        s_list = list(s)
        while left<right:
            if s[left] in vowels and s[right] in vowels:
                s_list[left],s_list[right]=s_list[right],s_list[left]
                left+=1
                right-=1
            elif s[left] in vowels and s[right] not in vowels:
                right-=1
            else:
                left+=1
        s = ''.join(s_list)
        return s
