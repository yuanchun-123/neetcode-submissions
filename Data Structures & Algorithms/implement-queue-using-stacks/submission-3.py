class MyQueue:

    def __init__(self):
        self.s = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        for i in range(len(self.s)):
            self.s2.append(self.s.pop())
        res = self.s2.pop()
        for j in range(len(self.s2)):
            self.s.append(self.s2.pop())
        return res

    def peek(self) -> int:
        return self.s[0]

    def empty(self) -> bool:
        return (len(self.s) == 0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()