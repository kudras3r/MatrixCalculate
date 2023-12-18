
class Buffer:
    def __init__(self):
        self.size: dict = {
            'matr1': {
                'rows': 3,
                'cols': 3,
            },
            'matr2': {
                'rows': 3,
                'cols': 3,
            }
        }
        
    def getRequestData(self, request):
        try:
            self.firstMatrixData: list = [int(x) if x != '' else 0 for x in request.form.getlist('num1[]')]
            self.secondMatrixData: list = [int(x) if x != '' else 0 for x in request.form.getlist('num2[]')]
            self.sizeData: str = request.form.get('size').split('-')
            self.operation: str = request.form['oper']
            print("SDATA", self.secondMatrixData)
        except ValueError:
            return '400'

    def sizeUnpack(self):
        for item in self.sizeData[-2::-1]:
            s = [int(x) for x in item[7:10].split(';')]
            if item[5] == '1' and self.size['matr1']['rows'] == 3 and self.size['matr1']['cols'] == 3:
                self.size['matr1']['rows'] = s[0]
                self.size['matr1']['cols'] = s[1]
            elif item[5] == '2' and self.size['matr2']['rows'] == 3 and self.size['matr2']['cols'] == 3:
                self.size['matr2']['rows'] = s[0]
                self.size['matr2']['cols'] = s[1]
    
    def takeMatrData(self, matrNum: int):
        if (matrNum == 1):
            matrKey = 'matr1'
            matr = self.firstMatrixData
        elif (matrNum == 2):
            matrKey = 'matr2'
            matr = self.secondMatrixData
        matrData = {
                'nums': matr,
                'rows': self.size[matrKey]['rows'], 
                'cols': self.size[matrKey]['cols'] 
            }      
        return matrData
        
    

        
        
    

#def sieUnpack(sizeData: str):
#    for item in sizeData[-2::-1]:
#        s = [int(x) for x in item[7:10].split(';')]
#        if item[5] == '1' and size['matr1']['rows'] == 3 and size['matr1']['cols'] == 3:
#            size['matr1']['rows'] = s[0]
#            size['matr1']['cols'] = s[1]
#        elif item[5] == '2' and size['matr2']['rows'] == 3 and size['matr2']['cols'] == 3:
#            size['matr2']['rows'] = s[0]
#            size['matr2']['cols'] = s[1]