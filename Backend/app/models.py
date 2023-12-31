from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    img = db.Column(db.String(100))
    url = db.Column(db.String(200))
    price = db.Column(db.String(100))
    timeline = db.Column(db.String(100))
    location = db.Column(db.String(200))
    lon = db.Column(db.Float)
    lat = db.Column(db.Float)
    description = db.Column(db.String(1000))