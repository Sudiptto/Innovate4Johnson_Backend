from flask import Blueprint, render_template, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from .models import *

users = Blueprint("users", __name__)


@users.route("/getAllUsers", methods=["GET"])
def getAllUsers():
    users = Canidate.query.all()
    users_list = [user.to_dict1() for user in users]
    return jsonify(users_list)
