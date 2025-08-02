class Solution:
    def trap(self, height: List[int]) -> int:
        left_max=[0]*len(height)
        right_max=[0]*len(height)
        count=0
        left_max[0]=height[0]
        right_max[-1]=height[-1]
        for i in range(len(height)-1):
            left_max[i]=max(left_max[i-1],height[i])
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        for i in range (len(height)):
            count += max(0, min(left_max[i], right_max[i]) - height[i])
        return count

        




