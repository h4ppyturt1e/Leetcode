from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = {}
        
        for num in nums:
            if num not in numsDict:
                numsDict[num] = 1
            else:
                numsDict[num] += 1
        
        return sorted(numsDict, key=numsDict.get, reverse=True)[:k]