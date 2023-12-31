import sys
from app import app, db
from app.models import Project
from flask import Flask, jsonify
from Scraper.main import scrape_all
import requests


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
                    county = display_name_parts[2] 
                    dbProject.county = county
                else:
                    dbProject.county = scrape_project.get('county')
                dbProject.lat = latitude
                dbProject.lon = longitude
        db.session.add(dbProject)
    db.session.commit()
    return jsonify({"message": "Received data successfully"}),200