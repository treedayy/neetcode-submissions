class Solution:
    import math
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(len(points)):
            xi = points[i][0]
            yi = points[i][1]
            distance = math.sqrt(xi**2 + yi**2)
            minHeap.append((distance, points[i]))
        heapq.heapify(minHeap)
        
        #print(minHeap)
        closest = []
        for i in range(k):
            val = heapq.heappop(minHeap)
            closest.append(val[1])

        return closest