import sys
from app import app,db
from app.models import Project
from flask import Flask, jsonify
from Scraper.main import scrape_all
import requests
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
    url = 'https://nominatim.openstreetmap.org/search'
    scrape_projects = scrape_all()

    for scrape_project in scrape_projects:
        dbProject = Project()
        dbProject.description = scrape_project.get('description')
        dbProject.name = scrape_project.get('name')
        dbProject.price = scrape_project.get('price')
        dbProject.img = scrape_project.get('img')
        dbProject.url = scrape_project.get('url')
        dbProject.location = scrape_project.get('location')
        dbProject.timeline = scrape_project.get('timeline')
        params = {'q':scrape_project.get('location'), 'format': 'json'} 
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            
            
           
        

