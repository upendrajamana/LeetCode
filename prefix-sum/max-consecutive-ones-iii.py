class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window_length=0
        l=r=0
        zeros=0
        maxi=0
        for r in range(len(nums)):
            if nums[r]==0:
                zeros+=1
            while zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            window_length=r-l+1
            maxi=max(maxi,window_length)
        return maxi



            

        