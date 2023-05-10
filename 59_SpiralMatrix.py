from typing import List

def smartPrint(res):
    for line in res:
        print(line)
    
    print()

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        dirDict = {
            0: (0, 1),
            1: (1, 0),
            2: (0, -1),
            3: (-1, 0)
        }
        
        result = [[0 for _ in range(n)] for _ in range(n)]
        
        curDir = 0
        curNum = 1
        
        i, j = 0, 0
        
        # n passes for first iteration
        for x in range(n):
            result[i][j] = curNum
            # print(i, j)
            
            di, dj = dirDict[curDir]
            
            if x != n-1:
                i, j = i + di, j + dj
                curNum += 1
        curDir = (curDir + 1) % 4
            
        for x in range(n-1, 0, -1):
            for _ in range(2):
                for y in range(x):
                    result[i][j] = curNum
                    # print(i, j)
                    
                    di, dj = dirDict[curDir]
                    
                    if y != n-1:
                        i, j = i + di, j + dj
                        curNum += 1
                curDir = (curDir + 1) % 4
        
        result[i][j] = curNum

        return result
    
    
if __name__ == '__main__':
    n = 5
    result = Solution().generateMatrix(n)
    
    smartPrint(result)

