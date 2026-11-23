class MyQueue:

    def __init__(self):
        self.s= []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s.append(x)
        

    def trans(self):
        if not self.s2:
            while self.s:
                self.s2.append(self.s.pop())

    def pop(self) -> int:
        self.trans()
        return self.s2.pop()
        
    def peek(self) -> int:

        self.trans()
        x = self.s2.pop()
        self.s2.append(x)
        return x
        

    def empty(self) -> bool:
        return not self.s2 and not self.s
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()