"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        h = []
        intervals.sort(key=lambda x: x.start)

        for i in intervals:
            if h and i.start >= h[0]:
                heapq.heappop(h)
            heapq.heappush(h, i.end)

            res = max(res, len(h))
        
        return res