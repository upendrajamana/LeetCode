class Solution:
    def permuteUnique(self, l: List[int]) -> List[List[int]]:
        def dfs(path,used,res):
            if len(path)==len(l):
                res.append(path[:])
                return
            for i,ele in enumerate(l):
                if used[i]:
                    continue
                path.append(ele)
                used[i]=True
                dfs(path,used,res)
                path.pop()
                used[i]=False
        res=[]
        dfs([],[False]*len(l),res)
        unique_permutations=list(map(list,set(map(tuple,res))))
        return unique_permutations