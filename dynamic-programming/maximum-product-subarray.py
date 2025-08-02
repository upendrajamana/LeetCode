class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left_product=1
        right_product=1
        ans=nums[0]
        for i in range(len(nums)):
            if left_product==0:
                left_product=1
            if right_product == 0:
                right_product = 1
            left_product*=nums[i]
            right_product*=nums[len(nums)-1-i]
            ans=max(ans,max(left_product,right_product))
        return ans