class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash_map={}
        longest_length=1
        for i in range(len(nums)):
            hash_map[nums[i]]=False
        for i in nums:
            current_length=1
            next_num=i+1
            while next_num in hash_map and hash_map[next_num]==False:
                current_length+=1
                hash_map[next_num]=True
                next_num+=1
            prev_num=i-1
            while prev_num in hash_map and hash_map[prev_num]==False:
                current_length+=1
                hash_map[prev_num]=True
                prev_num-=1
            longest_length=max(longest_length,current_length)
        return longest_length

        


