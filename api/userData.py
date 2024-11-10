from flask import Blueprint, render_template, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from .models import *


userData = Blueprint("userData", __name__)

# test route
# Sample output:
"""
{
    "canidates": [
        {
            "firstName": "John",
            "lastName": "Doe",
            "id": 1
        },
        {
            "firstName": "Jane",
            "lastName": "Doe",
            "id": 2
        },
        ...
    ]
}
"""
@userData.route("/listUser", methods=["GET"])
def test():
    # return a list of all canidates -> have first name / last name / user-id 
    canidates = Canidate.query.all()
    
    # get in this format -> NOTE the canidates there is no .to_dict() method
    # Construct the response manually
    response = {
        "canidates": [
            {
                "firstName": canidate.firstName,
                "lastName": canidate.lastName,
                "id": canidate.id
            }
            for canidate in canidates
        ]
    }
    return jsonify(response)

# route for getting a specific user (more data, takes in user_id)
# Sample output:
"""
{
    "firstName": "John",
    "lastName": "Doe",
    "username": "johndoe",
    "email": "
    "gradDate": "2023",
    ...
}
"""

@userData.route("/getUser/<id>", methods=["GET"])
def getUser(id):
    # get the user by id
    canidate = Canidate.query.get(id)
    
    # Construct the response manually
    response = {
        "firstName": canidate.firstName,
        "lastName": canidate.lastName,
        "username": canidate.username,
        "email": canidate.email,
        "gradDate": canidate.gradDate,
        "location": canidate.location,
        "linkedIn": canidate.linkedIn,
        "github": canidate.github
    }
    return jsonify(response)