from datetime import datetime

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user
from dotenv import load_dotenv
from werkzeug.security import check_password_hash, generate_password_hash

import sys
import os
from config import CALC_PATH

sys.path.insert(0, CALC_PATH)
from calculate import Matrix
from app import app, db
from helpers import Buffer
from models import User

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
    return render_template("index.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    login = request.form.get("login")
    password = request.form.get("password")
    password2 = request.form.get("password2")

    if request.method == "POST":
        if not (login or password or password2):
            flash("Please fill all fields!")
        elif password2 != password:
            flash("Passwords fields is not equal!")
        else:
            hash_pwd = generate_password_hash(password)
            new_user = User(id=1223, login=login, password=hash_pwd)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login"))
    return render_template("auth/register.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    login = request.form.get("login")
    password = request.form.get("password")
    print(login, type(login))
    if login and password:
        user = User.query.filter_by(login=login).first()
        print(user)
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("mode"))
        else:
            flash("Login or password is incorrect!")
            return redirect(url_for("login"))

    else:
        flash("Please fill Login and Password in fields!")
        return render_template("auth/login.html")


@app.route("/logout", methods=["POST", "GET"])
def logout():
    pass


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
