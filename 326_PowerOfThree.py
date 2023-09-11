
class Solution:
    def isPowerOfThree(self, n: int):
        if n <= 0: return False
        cur = 1
        for _ in range(38):
            if cur == n: return True
            cur = cur * 3
        
        return False
    
    