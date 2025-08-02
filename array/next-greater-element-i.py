class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map={n:i for i,n in enumerate(nums1)}
        res=[-1]*len(nums1)
        stack=[]
        for i in nums2:
            while stack and i>stack[-1]:
                val=stack.pop()
                idx=hash_map[val]
                res[idx]=i
            if i in hash_map:
                stack.append(i)
        return res