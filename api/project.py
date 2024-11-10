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
