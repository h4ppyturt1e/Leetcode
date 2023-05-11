class ProductOfNumbers:
    
    def __init__(self):
        self.nums = [1]
        self.products = [1]
        self.size = 0
        self.last_zero = -1

    def add(self, num: int) -> None:
        if self.last_zero >= 0:
            self.last_zero += 1
        
        if num < 0 or num > 100:
            return
        self.size += 1
        
        self.nums.append(num)
        
        if num == 0:
            self.products.append(self.products[-1])
            self.last_zero = 0
        else:
            self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        if self.size == 0:
            return 0
        
        if self.last_zero >= 0 and self.last_zero < k:
            return 0
        
        return self.products[-1] // self.products[-1-k]
    
if __name__ == '__main__':
    tester = [[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
    
    solve = ProductOfNumbers()
    
    for i in tester:
        i = i[0]
        solve.add(i)
        
    