class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        frequency={}
        for i in nums:
            if i in frequency:
                frequency[i]+=1
            else:
                frequency[i]=1
        heap=[]
        for num,freq in frequency.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for freq,num in heap]