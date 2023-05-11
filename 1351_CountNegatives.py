from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        negs = 0
        for row in grid:
            print(row[::-1])
            for val in row[::-1]:
                if val >= 0:
                    break
                else: 
                    negs += 1
            total += negs
        return total
        
if __name__ == '__main__':
    grid_list = [
        [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]],
        [[3,2],[1,0]],
        [[7,6,6,6,3,2,-3]],
        [[8,-2,-2,-2,-4,-5,-5],[-2,-3,-3,-4,-4,-5,-5],[-2,-5,-5,-5,-5,-5,-5],[-3,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5]],
        [[15,14,13,13,12,11,10,9,9,8,7,7,7,6,6,6,5,4,1,-15]],
        [[20,-8,-9,-10,-10,-11,-11,-11,-12,-12,-12,-12,-12,-16,-16,-17,-18,-19,-20,-20]]
    ]
    
    for grid in grid_list:
        solve = Solution()
        total = solve.countNegatives(grid)
        print(total)
        print("========================")