from  collections import Counter
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res=[]
        res+=set(nums1).intersection(nums2)
        res+=set(nums1).intersection(nums3)
        res+=set(nums2).intersection(nums3)
        return list(set(res))
