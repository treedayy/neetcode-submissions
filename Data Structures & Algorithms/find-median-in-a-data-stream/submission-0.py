class MedianFinder:

    def __init__(self):
        #max heap
        self.lower = []
        #min heap
        self.upper = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -num)
        if self.lower and self.upper:
            if -self.lower[0] > self.upper[0]:
                val = -heapq.heappop(self.lower)
                heapq.heappush(self.upper, val)
        if len(self.lower) > len(self.upper) + 1:
            val = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, val)
        elif len(self.upper) > len(self.lower):
            val = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -val)
        

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return (-self.lower[0])
        return (-self.lower[0] + self.upper[0]) / 2
        
        