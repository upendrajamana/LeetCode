class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini=float('inf')
        left=0
        total=0
        for right in range(len(nums)):  
            total+=nums[right]
            while total>=target:
                curr_length=right-left+1
                mini=min(mini,curr_length)
                total-=nums[left]
                left+=1
        return mini if mini!=float('inf') else 0
                
            
            
