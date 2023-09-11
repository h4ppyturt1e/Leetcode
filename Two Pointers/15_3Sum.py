from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numSet = set(nums)
        nums = sorted(nums)
        
        for i in range(1, len(nums)-1):
            cur = nums[i]
            
            
            
    
if __name__ == '__main__':
    soln = Solution()
    res = soln.threeSum([3,0,-2,-1,1,2])
    print(res)