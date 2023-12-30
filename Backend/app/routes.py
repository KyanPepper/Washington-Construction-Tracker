import sys
from app import app,db
from app.models import Project
from flask import Flask, jsonify

@app.before_request
def initDB(*args, **kwargs):
    if app.got_first_request:
        db.create_all()

@app.route('/test', methods=['POST','GET'])
def testpost():
    print('testing')



