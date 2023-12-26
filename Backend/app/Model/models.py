from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    img = db.Column(db.String(1000))
    url = db.Column(db.String(1000))
    price = db.Column(db.String(1000))
    timeline = db.Column(db.String(100))
    address = db.Column(db.String(255))
    location = db.Column(db.String(255))
    description = db.Column(db.String(1000))
