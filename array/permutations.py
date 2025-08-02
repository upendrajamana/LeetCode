class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(path,used,res):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i]=True
                dfs(path,used,res)
                path.pop()
                used[i]=False
        dfs([],[False]*len(nums),res)
        return res

            