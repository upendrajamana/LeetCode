class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if (mid == 0 or nums[mid] != nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] != nums[mid + 1]):
                return nums[mid]
            left=mid-1 if nums[mid-1]==nums[mid] else mid
            if left%2:
                high=mid-1
            else:
                low=mid+1

            