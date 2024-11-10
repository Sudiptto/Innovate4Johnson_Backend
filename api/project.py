from flask import Blueprint, render_template, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from .models import *


project = Blueprint("project", __name__)


# works
@project.route("/getAllTeams", methods=["GET"])
def getAllTeams():
    teams = canidateTeams.query.all()
    teams_list = [team.to_dict() for team in teams]
    return jsonify(teams_list)

new_user = Canidate(
    firstName=first_name,
    lastName=last_name,
    username=username,
    email=email,
    gradDate=gradDate,
    location=location,
    password_hash=password_hash,
    linkedIn=linkedIn,
    github=github,
    resumeUrl=resumeUrl,
    date_created=datetime.utcnow()
)

# Add user to the database
db.session.add(new_user)
db.session.commit()