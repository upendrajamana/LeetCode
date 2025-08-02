class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for idx,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackt,stackidx=stack.pop()
                res[stackidx]=idx-stackidx
            stack.append([t,idx])
        return res
        

