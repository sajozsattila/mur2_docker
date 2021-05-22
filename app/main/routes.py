from flask import jsonify, current_app, send_from_directory
# blueprint
from app.main import bp

# global values
from flask import g

# check before every request
@bp.before_request
def before_request():
    pass

# after every request
@bp.after_request
def set_response_headers(response):
    return response

@bp.route('/')
def root():
    return jsonify({"name": current_app.config['NAME'], 'version': current_app.config['VERSION']})


