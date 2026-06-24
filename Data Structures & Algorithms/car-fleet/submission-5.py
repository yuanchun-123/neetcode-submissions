class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = len(speed)
        times = []
        info = []

        for i in range(len(speed)):
            info.append((position[i], speed[i]))
        info.sort(reverse = True)

        for pos, s in info:
            time = (target - pos) / s
            
            if times and time <= times[-1]:
                continue
            else:
                times.append(time)

        return len(times)




