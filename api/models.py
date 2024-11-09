"""
File Description: Get the user model (database)
"""
from . import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# For Canidate 
class Canidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(150), nullable=False)
    lastName = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    location = db.Column(db.String(150), nullable=False)
    gradDate = db.Column(db.String(150), nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)

    # helper functions for password hashing
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
    

# for Recruiter / Hiring Manager 
class Recruiter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(150), nullable=False)
    lastName = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    location = db.Column(db.String(150), nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)

    # helper functions for password hashing
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


# for innovation challenge posting from recruiter
class InnovationChallenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    # either 6 - 8 team size integer
    teamSize = db.Column(db.Integer, nullable=False)

    date_started = db.Column(db.DateTime, nullable=False)
    date_ended = db.Column(db.DateTime, nullable=False)

    # foreign key -> recruiter_id (recruiter who posted the challenge) 
    recruiter_id = db.Column(db.Integer, db.ForeignKey('recruiter.id'), nullable=False)
    recruiter = db.relationship('Recruiter', backref='innovation_challenge')