from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    img = db.Column(db.String(1000))
    url = db.Column(db.String(1000))
    price = db.Column(db.Double ,default = 0)
    started_at = db.Column(db.DateTime)
    expected_done = db.Column(db.DateTime)
    address = db.Column(db.String(255))
    location = db.Column(db.String(255))
    description = db.Column(db.String(1000))
