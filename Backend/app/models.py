from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    img = db.Column(db.String(500))
    url = db.Column(db.String(200))
    price = db.Column(db.String(200))
    timeline = db.Column(db.String(300))
    location = db.Column(db.String(200))
    lon = db.Column(db.Float)
    lat = db.Column(db.Float)
    description = db.Column(db.String(1000))
    county = db.Column(db.String(100))


    def truncate_values(self):
        self.name = self.name[:100] if self.name else None
        self.img = self.img[:500] if self.img else None
        self.url = self.url[:200] if self.url else None
        self.price = self.price[:200] if self.price else None
        self.timeline = self.timeline[:300] if self.timeline else None
        self.location = self.location[:200] if self.location else None
        self.description = self.description[:1000] if self.description else None
        self.county = self.county[:100] if self.county else None