class StockSpanner:

    def __init__(self):
        self.p = [] #(price, index)

    def next(self, price: int) -> int:
        res = 1
        while self.p and self.p[-1][0] <= price:
            res += self.p[-1][1]
            self.p.pop()
        self.p.append((price, res))
        return res


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)