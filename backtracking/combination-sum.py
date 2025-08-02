class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def backtrack(temp,total,start):
            if total==target:
                result.append(temp[:])
                return
            if total>target:
                return 
            
            for i in range(start,len(candidates)):
                temp.append(candidates[i])
                backtrack(temp, total + candidates[i],i)
                temp.pop()
                
        backtrack([], 0, 0)
        return result

