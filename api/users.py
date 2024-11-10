from flask import Blueprint, render_template, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from .models import *

users = Blueprint("users", __name__)


@users.route("/getAllUsers/<user_id>", methods=["GET"])
def getAllUsers(user_id):
    user = Canidate.query.get(user_id)
    if user:
        return jsonify(user.to_dict1())
    return jsonify({"error": "User not found"}), 404
