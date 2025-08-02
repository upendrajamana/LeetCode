class Solution:
    def makeGood(self, s: str) -> str:
        result=[]
        for i in s:
            if result and abs(ord(result[-1])-ord(i))==32:
                result.pop()
            else:
                result.append(i)
        return ''.join(result)
                

            
