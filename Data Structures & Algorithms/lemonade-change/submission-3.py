class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        x, y = 0, 0
        for b in bills:
            if b == 5:
                x += 1
            elif b == 10:
                x -= 1
                y += 1
            else:
                if y > 0:
                    y -= 1
                    x -= 1
                else:
                    x -= 3
            if x < 0 or y < 0:
                return False
        return True