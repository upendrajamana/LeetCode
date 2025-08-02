class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        def backtrack(temp,start):
            result.append(list(temp))
            for i in range(start,len(nums)):
                temp.append(nums[i])
                backtrack(temp,i+1)
                temp.remove(nums[i])
            
        backtrack([],0)
        return result

        