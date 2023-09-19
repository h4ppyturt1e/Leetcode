from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        
        leftMax = height[0]
        rightMax = height[-1]
        
        leftWalls = []
        rightWalls = []
        
        for i in range(len(height)):
            curLeft = height[left+i]
            curRight = height[right-i]
            
            if curLeft >= leftMax:
                leftWalls.append(left+i)
                # leftWalls[left+i] = curLeft
                leftMax = curLeft
            
            if curRight >= rightMax:
                rightWalls.append(right-i)
                # rightWalls[right-i] = curRight
                rightMax = curRight
        
        total = 0
        seen = set()
        # print(f"leftWalls: {leftWalls}")
        # print(f"rightWalls: {rightWalls}")
        
        for j in range(len(leftWalls)-1):
            a, b = leftWalls[j], leftWalls[j+1]
            if (a,b) in seen: continue
            diff = abs(a - b) - 1
            if diff < 1: continue
            rect = (min(height[a],height[b]) * diff)
            blocks = sum(height[a+1:b])
            # print(f"a: {a}, b: {b}, diff: {diff}")
            # print(f"rect: {rect}, blocks: {blocks}")
            total += (rect - blocks)
            seen.update([(a,b)])
            

        for k in range(len(rightWalls)-1):
            a, b = rightWalls[k], rightWalls[k+1]
            if (b,a) in seen: continue
            diff = abs(a - b) - 1
            if diff < 1: continue
            rect = (min(height[a],height[b]) * diff)
            blocks = sum(height[b+1:a])
            # print(f"a: {a}, b: {b}, diff: {diff}")
            # print(f"rect: {rect}, blocks: {blocks}")
            total += (rect - blocks)
            seen.update([(b,a)])
        
        return total