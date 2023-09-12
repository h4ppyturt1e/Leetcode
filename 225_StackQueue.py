class MyStack:
    data = []
    topStack = None
    
    def __init__(self):
        self.data = []
    
    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        if not self.data: return
        res = self.top()
        self.data = self.data[:-1]
        return res

    def top(self) -> int:
        return self.data[-1]

    def empty(self) -> bool:
        return self.data == []


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()