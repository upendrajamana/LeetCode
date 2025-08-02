class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def is_sorted(a,b,c,d):
            if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
                return True
        

        h={}
        for i in range(len(nums)):
            h[nums[i]]=i
        s=set()
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    desired=target-nums[i]-nums[j]-nums[k]
                    if desired in h and is_sorted(i,j,k,h[desired]):
                        d=tuple(sorted([nums[i],nums[j],nums[k],nums[h[desired]]]))
                        s.add(d)
        return [list(quad) for quad in s]




