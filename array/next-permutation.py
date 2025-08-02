class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #here what's this logic behind this solution is from end to start of an array if the numbers are in increasing order we can do any greater number so if the current nums[i] is less than nums[i+1] then we create a greater permuation so we agin itering from backwards to create a next greater permutation by sorting the elements next to the swaped element
        bp = -1
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                bp=i
                break
        if bp==-1:
            nums[:] = reversed(nums[:])
            return 
        for i in range(n-1,bp-1,-1):
            if nums[i]>nums[bp]:
                nums[i],nums[bp]=nums[bp],nums[i]
                break
        nums[bp+1:]=sorted(nums[bp+1:])

            
