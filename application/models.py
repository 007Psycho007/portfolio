from main import db
from sqlalchemy.dialects.sqlite import TEXT, JSON

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    type = db.Column(db.String(255), unique=False)
    description = db.Column(db.String(255), unique=False)
    long_description = db.Column(TEXT(), unique=False)
    url = db.Column(db.String(255), unique=False, nullable=True)
    used_technologies = db.Column(JSON(), unique=False, nullable=False)
    features = db.Column(JSON(), unique=False, nullable=False)
    def __repr__(self):
        return f'<Project: {self.name}>'
    
class Technologies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    level = db.Column(db.Integer)
    
    def __repr__(self):
        return f'<Skill: {self.name}>'
    
class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    short_desc = db.Column(db.String(255), unique=False, nullable=False)
    
