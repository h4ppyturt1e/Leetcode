from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sortedNums = sorted(set(nums))
        longest = 1
        curlen = 1
        prev = sortedNums[0]
        for n in sortedNums[1:]:
            if prev + 1 == n:
                curlen += 1
            else:
                if curlen > longest:
                    longest = curlen
                curlen = 1
            prev = n
        
        if curlen > longest:
            return curlen
        return longest
                    
        
            
        