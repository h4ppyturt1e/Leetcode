from typing import List

class Cashier:
    
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        priceDict = {}
        
        for i in range(len(products)):
            priceDict[products[i]] = prices[i]
            
        self.n = n
        self.discount = discount
        self.priceDict = priceDict
        self.curCust = 1

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0
        
        isDiscount = False
        if self.curCust % self.n == 0:
            isDiscount = True
        
        for i in range(len(product)):
            total += self.priceDict[product[i]] * amount[i]
            
        if isDiscount:
            total = total * (1 - self.discount / 100)
        
        self.curCust += 1
        
        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)