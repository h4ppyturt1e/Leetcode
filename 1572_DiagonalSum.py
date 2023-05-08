class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        matSize = len(mat)
        totalSum = 0
        
        # left pointer and right pointer
        for leftPtr in range(matSize):
            rightPtr = matSize - 1 - leftPtr
            if leftPtr == rightPtr:
                totalSum += mat[leftPtr][rightPtr]
            else:
                totalSum += mat[leftPtr][leftPtr] + mat[leftPtr][rightPtr]
        
        return totalSum
    
