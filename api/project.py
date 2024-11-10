from flask import Blueprint, render_template, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from .models import *


project = Blueprint('project', __name__)

# works
@project.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Test route'}) 