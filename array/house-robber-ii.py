class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[-1]
        if len(nums) == 2:
            return max(nums)
        without_last=[]
        without_first=[]
        without_last.append(nums[0])
        without_last.append(max(nums[0],nums[1]))
        for  i in range(2,len(nums)-1):
            without_last.append(max((without_last[i-2]+nums[i]),without_last[i-1]))
        without_first=[]
        without_first.append(nums[1])
        without_first.append(max(nums[1],nums[2]))
        for  i in  range(3,len(nums)):
            without_first.append(max((without_first[i-3]+nums[i]),without_first[i-2]))
        return max(without_last[-1],without_first[-1])

        