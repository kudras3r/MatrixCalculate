from datetime import datetime

from flask import render_template, request, redirect, url_for
from dotenv import load_dotenv

import sys
import os
from config import CALC_PATH

sys.path.insert(0, CALC_PATH)
from calculate import Matrix
from app import app
from helpers import Buffer

load_dotenv()


def logRequest(request):
    with open("sessions.log", "a") as file:
        log = f"[ {datetime.now()} | {request.user_agent} ]"
        print(log, file=file)


@app.route("/view_logs")
def viewLogs():
    secretKey = request.args.get("key")
    if secretKey == os.getenv("KEY"):
        with open("sessions.log", "r") as file:
            logsData = [x.split("|") for x in file.readlines()]
        return render_template("logs.html", logs=logsData)
    else:
        response = "Incorrect url key!"
        return render_template("error.html", code="400", response=response)


@app.route("/", methods=["POST", "GET"])
def index():
    logRequest(request=request)
    # return redirect(url_for('mode'))
    return render_template("index.html")


@app.route("/mode", methods=["POST", "GET"])
def mode():
    return render_template("mode.html")


@app.route("/tables", methods=["POST", "GET"])
def aaa():
    userChoose = request.form["choose"]
    if userChoose == "2":
        return render_template("matr/two_matrs.html")
    elif userChoose == "1":
        return render_template("matr/one_matr.html")


@app.route("/calc/<string:set>", methods=["POST", "GET"])
def calc(set):
    buffer = Buffer()
    buffer.getRequestData(request, set)
    buffer.sizeUnpack()

    if set == "two_matrix":
        if buffer.response["req_code"] == 200:
            firstMatrix = Matrix(buffer.takeMatrData(1))
            secondMatrix = Matrix(buffer.takeMatrData(2))
            if buffer.operation == "➕":
                data = firstMatrix.summation(secondMatrix)
            elif buffer.operation == "✖":
                data = firstMatrix.multiply(secondMatrix)

            if data["calc"]["code"] == 200:
                return render_template(
                    "calc.html",
                    rows=data["rows"],
                    cols=data["cols"],
                    matrix=data["matr"],
                )
            else:
                return render_template(
                    "error.html",
                    code=data["calc"]["code"],
                    response=data["calc"]["mess"],
                )
        else:
            return render_template(
                "error.html",
                code=buffer.response["req_code"],
                response=buffer.response["mess"],
            )
    elif set == "one_matrix":
        if buffer.response["req_code"] == 200:
            firstMatrix = Matrix(buffer.takeMatrData(1))
            if buffer.operation == "transpose":
                data = firstMatrix.transpose()
                if data["calc"]["code"] == 200:
                    return render_template(
                        "calc.html",
                        rows=data["rows"],
                        cols=data["cols"],
                        matrix=data["matr"],
                    )
                else:
                    return render_template(
                        "error.html",
                        code=data["calc"]["code"],
                        response=data["calc"]["mess"],
                    )
            elif buffer.operation == "determin":
                data = firstMatrix.findDet()
                if data["calc"]["code"] == 200:
                    return render_template(
                        "calc.html",
                        rows=data["rows"],
                        cols=data["cols"],
                        matrix=data["matr"],
                        det=data["det"],
                    )
                else:
                    return render_template(
                        "error.html",
                        code=data["calc"]["code"],
                        response=data["calc"]["mess"],
                    )
        else:
            print("aaaa")
            return render_template(
                "error.html",
                code=buffer.response["req_code"],
                response=buffer.response["mess"],
            )
