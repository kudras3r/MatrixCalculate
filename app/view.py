
from config import CALC_PATH
from app import app
from helpers import Buffer
from datetime import datetime
from flask import render_template, request, redirect, url_for, abort
import sys

sys.path.insert(0, CALC_PATH)
from calculate import Matrix


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

    buffer = Buffer()
    
    buffer.getRequestData(request)
    buffer.sizeUnpack()
    
    firstMatrix = Matrix(buffer.takeMatrData(1))
    secondMatrix = Matrix(buffer.takeMatrData(2))
    
    if buffer.operation == '➕':
        data = firstMatrix.summation(secondMatrix)
        if data != '400':
            rows, cols = data['rows'], data['rows']
            matr = data['matr']
        else:
            response = 'Size error!'
            return render_template('error.html', code='400', response=response)
    
    elif buffer.operation == '✖':
        data = firstMatrix.multiply(secondMatrix)
        if data != '400':
            rows, cols = data['rows'], data['rows']
            matr = data['matr']
        else:
            response = 'Size error!'
            return render_template('error.html', code='400', response=response)    
    return render_template('calc1.html', rows=data['rows'], cols=data['cols'], matrix=data['matr'])

@app.errorhandler(400)
def errorHandle(e):
    response = 'Please enter the correct value!'
    return render_template('error.html', code='400', response=response)
    

