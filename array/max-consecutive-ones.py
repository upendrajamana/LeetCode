class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        current_max=0
        for i in nums:
            if i==1:
                current_max+=1
                maxi=max(maxi,current_max)
            else:
                current_max=0
        return maxi

            