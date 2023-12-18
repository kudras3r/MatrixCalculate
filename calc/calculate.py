
import numpy as np

class Matrix:
    def __init__(self, data: dict):
        self.nums = data['nums']
        self.rows = data['rows']
        self.cols = data['cols']
        def matrInit():
            print(data)
            matr = []
            i = 0
            for row in range(self.rows):
                line = []
                for col in range(self.cols):
                    line.append(self.nums[i])
                    i += 1
                matr.append(line)
            return np.array(matr)
        self.matrix = matrInit() 

    
    def summation(self, matr2):
        try:
            data = {
                'matr': np.add(self.matrix, matr2.matrix),
                'rows': self.rows,
                'cols': self.cols,
            }
        except ValueError:
            return '400'
        return data
    
    def multiply(self, matr2):
        try:
            rows, cols = self.rows, matr2.cols
            data = {
                'matr': np.dot(self.matrix, matr2.matrix),
                'rows': rows,
                'cols': cols
            }
        except ValueError:
            return '400'
        return data
        
    

          
            
    



#print(a.)