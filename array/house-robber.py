class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[-1]
        result=[]
        result.append(nums[0])
        result.append(max(nums[0],nums[1]))
        for  i in range(2,len(nums)):
            val=max((nums[i]+result[i-2]),result[i-1])
            result.append(val)
        return result[-1]