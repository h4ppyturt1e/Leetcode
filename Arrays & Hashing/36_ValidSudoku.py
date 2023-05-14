from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check cols
        for row in board:
            rowSet = set()
            for n in row:
                if n == ".": 
                    continue
                if n in rowSet:
                    return False
                rowSet.add(n)
        
        # Check rows
        transposedBoard = [[None for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                transposedBoard[j][i] = board[i][j]
        
        for col in transposedBoard:
            colSet = set()
            for n in col:
                if n == ".": 
                    continue
                if n in colSet:
                    return False
                colSet.add(n)
        
        # Check boxes
        startPoints = [0, 3, 6]
        
        for i in startPoints:
            for j in startPoints:
                boxSet = set()
                for di in range(3):
                    for dj in range(3):
                        if board[i+di][j+dj] == ".": 
                            continue
                        if board[i+di][j+dj] in boxSet:
                            return False
                        boxSet.add(board[i+di][j+dj])
        
        return True