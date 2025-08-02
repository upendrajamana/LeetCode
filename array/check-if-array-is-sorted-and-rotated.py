class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Compare current and next element (circular comparison)
                count += 1
            if count > 1:  # If more than one break point, return False
                return False
        return True

            
