class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(res,s,left,right):
            if left==0 and right==0:
                res.append(s)
            if left>0:
                helper(res,s+'(',left-1,right)
            if right>0 and left<right:
                helper(res,s+')',left,right-1)
        res=[]
        helper(res,'',n,n)
        return res