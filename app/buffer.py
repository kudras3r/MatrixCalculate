"""

    Created, supported, updated by kudraser

    Contacts
    tg: https://t.me/kudras3r_dev
    GitHub: https://github.com/kudras3r
    vk: https://vk.com/dgcihf

"""


class Buffer:
    """
    This class makes the request to the site
    accept data and send it to view
    """

    def __init__(self):
        self.size: dict = {
            "matr1": {
                "rows": 3,
                "cols": 3,
            },
            "matr2": {
                "rows": 3,
                "cols": 3,
            },
        }
        self.response: dict = {
            "req_code": None,
        }

    def getRequestData(self, request, set):
        self._getGeneralData(request=request)
        self._getMatrixData(request=request, set=set)

    def _getGeneralData(self, request):
        self.sizeData: str = request.form.get("size").split("-")
        self.operation: str = request.form["oper"]
        self.response["req_code"] = 200

    def _getMatrixData(self, request, set):
        if set == "two_matrix":
            try:
                self.firstMatrixData: list = [
                    int(x) if x != "" else 0 for x in request.form.getlist("num1[]")
                ]
                self.secondMatrixData: list = [
                    int(x) if x != "" else 0 for x in request.form.getlist("num2[]")
                ]
                self.response["req_code"] = 200
            except ValueError:
                self.response["req_code"] = 406
                self.response["mess"] = "Incorrect value!"
        elif set == "one_matrix":
            try:
                self.firstMatrixData: list = [
                    int(x) if x != "" else 0 for x in request.form.getlist("num1[]")
                ]
                self.response["req_code"] = 200
            except:
                self.response["req_code"] = 406
                self.response["mess"] = "Incorrect value!"

    def sizeUnpack(self):
        if self.sizeData != [""]:
            for item in self.sizeData[-2::-1]:
                s = item.split(";")
                c = 0
                if c != 2:
                    matrKey = "matr1" if s[0][-1] == "1" else "matr2"
                    if (
                        self.size[matrKey]["rows"] == 3
                        and self.size[matrKey]["cols"] == 3
                    ):
                        self.size[matrKey]["rows"] = int(s[1])
                        self.size[matrKey]["cols"] = int(s[2].replace("|", ""))
                        c += 1

    def takeMatrData(self, matrNum: int):
        if matrNum == 1:
            matrKey = "matr1"
            matr = self.firstMatrixData
        elif matrNum == 2:
            matrKey = "matr2"
            matr = self.secondMatrixData
        matrData = {
            "nums": matr,
            "rows": self.size[matrKey]["rows"],
            "cols": self.size[matrKey]["cols"],
        }
        return matrData
