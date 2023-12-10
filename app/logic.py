
from flask import abort

class Matrix:
    
    def __init__(self, data: list, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.matrix: list[list] = self.matrixCreate(data, row, col)
        
    def matrixCreate(self, nums: list, row: int, col: int) -> list[list]:
        matrix = []
        i = 0
        for row in range(self.row):
            line = []
            for col in range(self.col):
                line.append(nums[i])
                i += 1
            matrix.append(line)
        return matrix
    
    def calculate(self, operation: str, matrix2) -> list[list]:
        if (operation == '➕'):
            if (matrix2.row == self.row and matrix2.col == self.col):   
                resultMatrix = [[0 for col in range(self.col)] for row in range(self.row)]
                for row in range(self.row):
                    for col in range(self.col):
                        resultMatrix[row][col] = matrix2.getItem(row, col) + self.getItem(row, col)
                return resultMatrix
            else:
                abort(400)
                
                
    def getItem(self, row: int, col: int) -> int:
        return self.matrix[row][col]

    def setItem(self, row: int, col: int, item: int) -> None:
        self.matrix[row][col] = item
    
    def trans(self):
        pass
    
    def onK(self):
        pass       
     
    def _get_readable_matrix(self, matrix):
        strings = []
        for row in matrix:
            strings.append(str(row))     
        return '\n'.join(strings)  
    
    def __str__(self):
        return self._get_readable_matrix(self.matrix)
    

                
        
    