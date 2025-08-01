from flask import Blueprint, jsonify
from app.services.utils import get_app_status

main = Blueprint('main', __name__)
api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/status')
def status():
    return jsonify(get_app_status())

@main.route('/')
def home():
    return 'Hello, World!'

@main.route('/about')
def about():
    return 'This is the about page.'
