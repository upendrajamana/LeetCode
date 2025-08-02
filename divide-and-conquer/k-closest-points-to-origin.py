import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for i in range(len(points)):
            x1,y1=points[i][0],points[i][1]
            distance = (x1-0)**2 + (y1-0)**2
            heapq.heappush(heap,(distance,points[i]))
        result=[]
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result


        

        