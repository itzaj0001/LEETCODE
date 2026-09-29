class StockSpanner:
    def __init__(self):
        self.st = []
        self.day = 0

    def next(self, price: int) -> int:
        self.day += 1

        while self.st and self.st[-1][1] <= price:
            self.st.pop()

        if not self.st:
            span = self.day
        else:
            span = self.day - self.st[-1][0]

        self.st.append([self.day, price])

        return span
  


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)