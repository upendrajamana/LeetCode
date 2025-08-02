class Solution:
    def isPerfectSquare(self, x: int) -> bool:
        if x==0:
            return 0
        low=1
        high=x
        while low<=high:
            mid=(low+high)//2
            if x//mid==x**0.5:
                return True
            elif mid>x//mid:
                high=mid-1
            else:
                low=mid+1
        return False