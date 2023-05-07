from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # nums index dict
        nums_dict = {}
        
        for i, num in enumerate(nums):
            if num in nums_dict:
                nums_dict[num].append(i)
            else:
                nums_dict[num] = [i]
        
        for num in nums:
            if target - num in nums_dict:
                if target - num == num:
                    if len(nums_dict[num]) > 1:
                        return nums_dict[num][:2]
                else:
                    return [nums_dict[num][0], nums_dict[target - num][0]]