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
    linkedIn = db.Column(db.String(250), nullable=False)
    github = db.Column(db.String(250), nullable=False)
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


# for canidate in the innovation challenge (all teams) (contains user_id, innovation_challenge_id, and team (regular id) )
class canidateTeams(db.Model):
    # Explicitly set the table name
    __tablename__ = 'canidateTeams'  


    # team number
    id = db.Column(db.Integer, primary_key=True)

    # semi-color separated list of user_ids, ex: 2;3;4;5;6
    user_ids = db.Column(db.String(5000), nullable=False)

    # foreign key -> innovation_challenge_id (what challenge is this for)
    innovation_challenge_id = db.Column(db.Integer, db.ForeignKey('innovation_challenge.id'), nullable=False)

    github_link = db.Column(db.String(150), nullable=False)
    figmaLink = db.Column(db.String(150), nullable=False)
    descriptionOfProject = db.Column(db.String(5000), nullable=False)
    
    # db relational
    innovation_challenge = db.relationship('InnovationChallenge', backref='canidateTeams')

# canidate to team -> easy mapping between user and team
class canidateToTeam(db.Model):

    __tablename__ = 'canidateToTeam'  

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('canidate.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('canidateTeams.id'), nullable=False)

    # db relational
    canidate = db.relationship('Canidate', backref='canidateToTeam')
    team = db.relationship('canidateTeams', backref='canidateToTeam')

