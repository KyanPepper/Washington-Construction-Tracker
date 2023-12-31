import sys
from app import app,db
from app.models import Project
from flask import Flask, jsonify
from Scraper.main import scrape_all
@app.before_request
def initDB(*args, **kwargs):
    if app.got_first_request:
        db.create_all()

@app.route('/test', methods=['POST','GET'])
def testpost():
    response = {'message': 'Received data successfully'}
    return jsonify(response), 200

@app.route('/scrapesites', methods=['POST','GET'])
def scrapesites():
    Projects = scrape_all()
    return jsonify(Projects),200
    
