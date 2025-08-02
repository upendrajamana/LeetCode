class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        part=[]
        def backtrack(i):
            if i==len(s):
                result.append(part.copy())
                return
            for j in range(i,len(s)):
                if self.is_palindrome(s,i,j):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
        
        backtrack(0)
        return result
    def is_palindrome(self,s,i,j):
        while i<=j:
            if s[i]!=s[j]:
                return False
            i,j=i+1,j-1
        return True
            
            