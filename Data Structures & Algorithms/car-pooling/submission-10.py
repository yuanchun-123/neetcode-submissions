class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        event = []
        for p, start, end in trips:
            event.append((start, p))
            event.append((end, -p))

        event.sort()
        count = 0

        for i, p in event:
            count += p

            if count > capacity:
                return False
            
        return True