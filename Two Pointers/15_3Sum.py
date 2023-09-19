from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        neg, zero, pos = [], [], []
        for num in nums:
            if num < 0:
                neg.append(num)
            elif num == 0:
                zero.append(num)
            else:
                pos.append(num)
                
        Neg = set(neg)
        Pos = set(pos)
        
        if zero:
            for num in Neg:
                if -num in Pos:
                    result.add((-num, 0, num))
        
        if len(zero) >= 3:
            result.add((0, 0, 0))
        
        for i in range(len(neg)):
            for j in range(i+1, len(neg)):
                target = -(neg[i] + neg[j])
                if target in Pos:
                    result.add(tuple(sorted([neg[i], neg[j], target])))
        
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                target = -(pos[i] + pos[j])
                if target in Neg:
                    result.add(tuple(sorted([pos[i], pos[j], target])))

        return list(result)
        
            
            
            
    
if __name__ == '__main__':
    soln = Solution()
    res = soln.threeSum([3,0,-2,-1,1,2])
    print(res)