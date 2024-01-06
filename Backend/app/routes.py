import sys
from app import app, db
from app.models import Project
from flask import Flask, jsonify
from Scraper.main import scrape_all
import requests
from sqlalchemy.sql.expression import func
from flask_cors import CORS

CORS(app)

@app.before_request
def initDB(*args, **kwargs):
    if app.got_first_request:
        db.create_all()


@app.route("/test", methods=["POST", "GET"])
def testpost():
    response = {"message": "Received data successfully"}
    return jsonify(response), 200


@app.route("/scrapesites", methods=["POST", "GET"])
def scrapesites():
    url = "https://nominatim.openstreetmap.org/search"
    scrape_projects = scrape_all()

    for scrape_project in scrape_projects:
        #boilerplate
        dbProject = Project()
        dbProject.description = scrape_project.get("description")
        dbProject.name = scrape_project.get("name")
        dbProject.price = scrape_project.get("price")
        dbProject.img = scrape_project.get("img")
        dbProject.url = scrape_project.get("url")
        dbProject.location = scrape_project.get("location")
        dbProject.timeline = scrape_project.get("timeline")
        #start logic
        params = {"q": scrape_project.get("location"), "format": "json"}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if len(data)> 0:
                latitude = float(data[0].get("lat", 0))
                longitude = float(data[0].get("lon", 0))
                if scrape_project.get('county') == None:
                    display_name_parts = data[0].get("display_name", "").split(", ")
                    for name in display_name_parts:
                        if 'County' in name:
                            county = name
                            dbProject.county = county
                else:
                    dbProject.county = scrape_project.get('county')
                dbProject.lat = latitude
                dbProject.lon = longitude
        db.session.add(dbProject)
    db.session.commit()
    return jsonify({"message": "Received data successfully"}),200

from flask import jsonify

@app.route('/getmap', methods=['GET'])
def getMapProjects():
    projects = Project.query.filter(Project.lat.isnot(None)).all()
    
    serialized_projects = [
        {
            'id': project.id,
            'name': project.name,
            'img': project.img,
            'url': project.url,
            'price': project.price,
            'timeline': project.timeline,
            'location': project.location,
            'lon': project.lon,
            'lat': project.lat,
            'description': project.description,
            'county': project.county,
        }
        for project in projects
    ]
    
    return jsonify(serialized_projects)

@app.route('/getproject/<projectid>', methods=['GET','POST'])
def getproject(projectid):
    project = Project.query.filter_by(id=projectid).first()
    
    serialized_projects = [
        {
            'id': project.id,
            'name': project.name,
            'img': project.img,
            'url': project.url,
            'price': project.price,
            'timeline': project.timeline,
            'location': project.location,
            'lon': project.lon,
            'lat': project.lat,
            'description': project.description,
            'county': project.county,
        }
    ]
    return jsonify(serialized_projects)

@app.route('/getsnoho', methods=['GET','POST'])
def getSnohomish():
    projects = Project.query.filter_by(county='Snohomish County').all()
    
    serialized_projects = [
        {
            'id': project.id,
            'name': project.name,
            'img': project.img,
            'url': project.url,
            'price': project.price,
            'timeline': project.timeline,
            'location': project.location,
            'lon': project.lon,
            'lat': project.lat,
            'description': project.description,
            'county': project.county,
        }
        for project in projects
    ]
    return jsonify(serialized_projects)


@app.route('/getking', methods=['GET','POST'])
def getKing():
    projects = Project.query.filter_by(county='King County').all()
    
    serialized_projects = [
        {
            'id': project.id,
            'name': project.name,
            'img': project.img,
            'url': project.url,
            'price': project.price,
            'timeline': project.timeline,
            'location': project.location,
            'lon': project.lon,
            'lat': project.lat,
            'description': project.description,
            'county': project.county,
        }
        for project in projects
    ]
    return jsonify(serialized_projects)

@app.route('/getspo', methods=['GET','POST'])
def getSpo():
    projects = Project.query.filter_by(county='Spokane County').all()
    
    serialized_projects = [
        {
            'id': project.id,
            'name': project.name,
            'img': project.img,
            'url': project.url,
            'price': project.price,
            'timeline': project.timeline,
            'location': project.location,
            'lon': project.lon,
            'lat': project.lat,
            'description': project.description,
            'county': project.county,
        }
        for project in projects
    ]
    return jsonify(serialized_projects)


@app.route('/getNC', methods=['GET','POST'])
def getNC():
    excluded_counties = ['Snohomish County', 'King County', 'Spokane County']
    projects = Project.query.filter(Project.county.notin_(excluded_counties)).all()
    serialized_projects = [
        {
            'id': project.id,
            'name': project.name,
            'img': project.img,
            'url': project.url,
            'price': project.price,
            'timeline': project.timeline,
            'location': project.location,
            'lon': project.lon,
            'lat': project.lat,
            'description': project.description,
            'county': project.county,
        }
        for project in projects
    ]
    return jsonify(serialized_projects)

@app.route('/getrand', methods=['GET','POST'])
def getRandom():
   
    projects =  Project.query .order_by(func.random()).limit(3).all()
    
    serialized_projects = [
        {
            'id': project.id,
            'name': project.name,
            'img': project.img,
            'url': project.url,
            'price': project.price,
            'timeline': project.timeline,
            'location': project.location,
            'lon': project.lon,
            'lat': project.lat,
            'description': project.description,
            'county': project.county,
        }
        for project in projects
    ]
    return jsonify(serialized_projects)

