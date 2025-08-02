class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff=float('inf')
        closest=0
        for i in range(len(nums)-2):
            low=i+1
            high=len(nums)-1
            while low<high:
                current_sum=nums[i]+nums[low]+nums[high]
                if abs(target-current_sum)<abs(diff):
                    diff=target-current_sum
                    current_sum=nums[i]+nums[low]+nums[high]
                    closest=current_sum
                elif current_sum<target:
                    low+=1
                elif current_sum>target:
                    high-=1
                else:
                    return current_sum
        return closest
