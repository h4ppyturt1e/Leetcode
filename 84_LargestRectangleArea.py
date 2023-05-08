from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        print(len(heights))
        
        # get longest consecutive sequence [O(nlogn)]
        sortedHeights = sorted(heights)
        maxHeight = sortedHeights[-1]
        
        maxArea = 0
        
        # get the largest area for each height [O(n^2)]
        # loops n times
        for curHeight in range(1, maxHeight+1):
            maxWidth = 0
            curWidth = 0
            
            # get the longest consecutive width of height h [O(n)]
            for h in heights:
                if h >= curHeight:
                    curWidth += 1
                else:
                    maxWidth = max(maxWidth, curWidth)
                    curWidth = 0
                
            maxWidth = max(maxWidth, curWidth)
            
            maxArea = max(maxArea, maxWidth * curHeight)
            
        return maxArea