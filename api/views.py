from flask import Blueprint, render_template, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from .models import *


views = Blueprint('views', __name__)

# works
@views.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Test route'}) 