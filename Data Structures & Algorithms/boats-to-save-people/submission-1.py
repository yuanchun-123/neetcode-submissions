class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        need = 0
        while r >= l:
            tar = limit - people[r]
            if people[l] <= tar:
                l += 1
            need += 1
            r -= 1
        return need

