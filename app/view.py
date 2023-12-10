
from app import app
from datetime import datetime
from flask import render_template, request, redirect, url_for, abort
from forms import MatrixForm, NumInput, Matrix
from logic import Matrix
from werkzeug.exceptions import BadRequest

def logRequest(request):
    with open('sessions.log', 'a') as file:
        log = f'[ {datetime.now()} | {request.user_agent} ]'
        print(log, file=file)

@app.route('/view_logs')
def viewLogs():
    secretKey = request.args.get('key')
    if secretKey == '1111':
        with open('sessions.log', 'r') as file:
            logsData = [x.split('|') for x in file.readlines()]
        return render_template('logs.html', logs=logsData) 
    else:
        response = 'Incorrect url key!'
        return render_template('error.html', code='400', response=response)

@app.route('/', methods=["POST", "GET"])
def index():
    logRequest(request=request)
    return render_template('index2.html')

@app.route('/calc', methods=["POST", "GET"])
def calc():
    try:
        firstMatrixData: list = [int(x) if x != '' else 0 for x in request.form.getlist('num1[]')]
        secondMatrixData: list = [int(x) if x != '' else 0 for x in request.form.getlist('num2[]')]
    except ValueError:
        abort(400)
    operation: str = request.form['oper']
    #firstMatrix = Matrix(firstMatrixData, 4, 2) # ПОКА ЧТО 3 на 3
    #secondMatrix = Matrix(secondMatrixData, 3, 3) # ПОКА ЧТО 3 на 3
    
    if operation == '➕':
        print(firstMatrixData)
        
        #res = firstMatrix.calculate('➕', secondMatrix)
        #print(firstMatrix.getItem(1, 1))
        #firstMatrix.setItem(0, 0, 5)
        #a = firstMatrix.getItem(0, 0)
        #print(a)
     #   a = firstMatrix.calculate('➕', secondMatrix)
     #   print(a)
        #print(firstMatrix.getItem(1, 1))
        #print(firstMatrixData)
        pass
        
    
    return render_template('calc1.html', nums=[[0,0,0],[0,0,0],[0,0,0]])

@app.errorhandler(400)
def errorHandle(e):
    response = 'Please enter the correct value!'
    return render_template('error.html', code='400', response=response)
    

