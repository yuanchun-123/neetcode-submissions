class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  #(item of index, temperature)
        for i, tem in enumerate(temperatures):
            while stack and stack[-1][1] < tem:
                idx, item = stack.pop()
                result[idx] = i - idx
            stack.append((i, tem))
        return result


