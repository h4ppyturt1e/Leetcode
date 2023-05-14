from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        totalWithZero = 1
        hasZero = False

        for n in nums:
            if n == 0:
                if hasZero:
                    return [0] * len(nums)
                totalProduct = 0
                hasZero = True
            else:
                totalProduct *= n
                totalWithZero *= n
        
        return [totalProduct // n if n != 0 else totalWithZero for n in nums]
        