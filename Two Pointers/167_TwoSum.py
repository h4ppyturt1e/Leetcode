from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 1
        right = len(numbers)
        
        total = numbers[left-1] + numbers[right-1]
        
        while total != target:
            if total > target:
                right -= 1
            
            elif total < target:
                left += 1
            
            total = numbers[left-1] + numbers[right-1]
        
        return [left, right]