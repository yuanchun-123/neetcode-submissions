class MedianFinder:

    def __init__(self):
        self.s = []
        self.l = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.s, -num)
        if (self.s and self.l and -self.s[0] > self.l[0]) \
        or (len(self.s) > len(self.l) + 1):
            val = heapq.heappop(self.s)
            heapq.heappush(self.l, -val)
        if len(self.l) > len(self.s) + 1:
            val = heapq.heappop(self.l)
            heapq.heappush(self.s, -val)

    def findMedian(self) -> float:
        if len(self.s) > len(self.l):
            return -self.s[0]
        elif len(self.l) > len(self.s):
            return self.l[0]
        else:
            return (-self.s[0] + self.l[0]) / 2.0


        
        
        





        