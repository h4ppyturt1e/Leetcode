from typing import List
from 

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        
        leftMax = height[0]
        rightMax = height[-1]
        
        wallsSet = set()
        
        for i in range(len(height)):
            curLeft = height[left+i]
            curRight = height[right-i]
            
            if curLeft >= leftMax:
                wallsSet.add(left+i)
                leftMax = curLeft
            
            if curRight >= rightMax:
                wallsSet.add(right-i)
                rightMax = curRight
        
        total = 0
        walls = sorted(list(wallsSet))
        
        for x in range(len(walls)-1):
            a, b = walls[x], walls[x+1]
            diff = abs(a - b) - 1
            if diff < 1: continue
            rect = (min(height[a],height[b]) * diff)
            blocks = sum(height[a+1:b])
            total += (rect - blocks)
        
        return total