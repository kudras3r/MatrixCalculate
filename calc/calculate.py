import numpy as np


class Matrix:
    def __init__(self, data: dict):
        self.nums = data["nums"]
        self.rows = data["rows"]
        self.cols = data["cols"]

        def matrInit():
            print(self.nums)
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
        data = {}
        try:
            data = {
                "matr": np.add(self.matrix, matr2.matrix),
                "rows": self.rows,
                "cols": self.cols,
                "calc": {
                    "code": 200,
                },
            }
        except IndexError:
            data["calc"] = {
                "code": 400,
                "mess": "Invalid size!",
            }
        except ValueError:
            data["calc"] = {
                "code": 400,
                "mess": "Invalid size!",
            }
        return data

    def multiply(self, item):
        data = {}
        if type(item) is not int:
            try:
                data = {
                    "matr": np.dot(self.matrix, item.matrix),
                    "rows": self.rows,
                    "cols": item.cols,
                    "calc": {
                        "code": 200,
                    },
                }
            except ValueError:
                data["calc"] = {
                    "code": 400,
                    "mess": "Invalid size!",
                }
        else:
            try:
                data = {
                    "matr": np.dot(item, self.matrix),
                    "rows": self.rows,
                    "cols": self.cols,
                    "calc": {
                        "code": 200,
                    },
                }
            except ValueError:
                data["calc"] = {
                    "code": 400,
                    "mess": "Invalid size!",
                }

        return data

    def transpose(self):
        data = {
            "matr": self.matrix.transpose(),
            "rows": self.cols,
            "cols": self.rows,
            "calc": {
                "code": 200,
            },
        }
        return data

    def findDet(self):
        data = {}
        try:
            data = {
                "matr": self.matrix,
                "rows": self.rows,
                "cols": self.cols,
                "calc": {
                    "code": 200,
                },
                "det": np.linalg.det(self.matrix),
            }
        except np.linalg.LinAlgError:
            data["calc"] = {
                "code": 406,
                "mess": "Invalid size! Det could be find only in square matrix!",
            }
        return data

    def inverse(self):
        data = {}
        try:
            data = {
                "matr": np.linalg.inv(self.matrix),
                "rows": self.rows,
                "cols": self.cols,
                "calc": {
                    "code": 200,
                },
            }
        except:
            data["calc"] = {
                "code": 406,
                "mess": "We could not find inverse matrix!",
            }
        return data


#
# pr#int(a.)
