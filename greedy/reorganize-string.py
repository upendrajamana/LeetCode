import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        #we use heap data structure for getting max frequent char every time
        maxHeap=[[-cnt,char] for char,cnt in count.items()]
        heapq.heapify(maxHeap)
        prev=None 
        res=""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            #this is for not again choosing the same char
            cnt,char=heapq.heappop(maxHeap)
            res += char
            cnt+=1
            #this means we had already a previous so we added
            if prev:
                heapq.heappush(maxHeap,prev)
                prev=None
            if cnt!=0:
                prev=[cnt,char]
        return res