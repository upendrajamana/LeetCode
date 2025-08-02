class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        def backtrack(temp,total,start):
            if total==target:
                result.append(temp[:])
            if total>target:
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                temp.append(candidates[i])
                backtrack(temp,total+candidates[i],i+1)
                temp.pop()
        backtrack([],0,0)
        return result