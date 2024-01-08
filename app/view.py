from datetime import datetime

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from dotenv import load_dotenv
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.exc import IntegrityError

import sys
import os
from config import CALC_PATH

sys.path.insert(0, CALC_PATH)
from calculate import Matrix
from app import app, db
from buffer import Buffer
from models import User

load_dotenv()


def logRequest(request):
    with open("sessions.log", "a") as file:
        log = f"[ {datetime.now()} | {request.user_agent} ]"
        print(log, file=file)


@app.route("/view_logs")
@login_required
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
            id = db.session.query(User).order_by(User.id.desc()).first().id + 1
            hash_pwd = generate_password_hash(password)
            new_user = User(id=id, login=login, password=hash_pwd)
            try:
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for("login"))
            except IntegrityError:
                flash("Login is not unique!")
                return redirect(url_for("register"))
    return render_template("auth/register.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    login = request.form.get("login")
    password = request.form.get("password")
    if login and password:
        user = User.query.filter_by(login=login).first()
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
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/mode", methods=["POST", "GET"])
@login_required
def mode():
    userName = current_user.login
    return render_template("mode.html", userName=userName)


@app.route("/tables", methods=["POST", "GET"])
@login_required
def takeMode():
    userChoose = request.form["choose"]
    userName = current_user.login
    if userChoose == "two matrixes":
        return render_template("matr/two_matrs.html", userName=userName)
    elif userChoose == "one matrix":
        return render_template("matr/one_matr.html", userName=userName)


@app.route("/calc/mode_<string:set>", methods=["POST", "GET"])
@login_required
def calc(set):
    buffer = Buffer()
    buffer.getRequestData(request, set)
    buffer.sizeUnpack()
    userName = current_user.login
    if buffer.response["req_code"] == 200:
        firstMatrix = Matrix(buffer.takeMatrData(1))
        if set == "two_matrix":
            secondMatrix = Matrix(buffer.takeMatrData(2))
            if buffer.operation == "➕":
                data = firstMatrix.summation(secondMatrix)
            elif buffer.operation == "✖":
                data = firstMatrix.multiply(secondMatrix)
        elif set == "one_matrix":
            if buffer.operation == "transpose":
                data = firstMatrix.transpose()
            elif buffer.operation == "determin":
                data = firstMatrix.findDet()
            elif buffer.operation == "inverse":
                data = firstMatrix.inverse()

        if data["calc"]["code"] == 200:

            def tryTakeDet():
                try:
                    return data["det"]
                except KeyError:
                    return ""

            return render_template(
                "calc.html",
                rows=data["rows"],
                cols=data["cols"],
                matrix=data["matr"],
                det=tryTakeDet(),
                userName=userName,
            )
        else:
            return render_template(
                "error.html",
                code=data["calc"]["code"],
                response=data["calc"]["mess"],
            )


@app.after_request
def redirectToSignin(response):
    if response.status_code == 401:
        return redirect(url_for("login"))
    return response
