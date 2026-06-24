class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        L, R = float('inf'), -float('inf')
        for num, start, end in trips:
            L = min(L, start)
            R = max(R, end)
        N = R - L + 1
        counts = [0] * N

        for num, start, end in trips:
            counts[start-L] += num
            counts[end-L] -= num

        i = 0
        for count in counts:
            i += count
            if i > capacity:
                return False
        return True


            
        