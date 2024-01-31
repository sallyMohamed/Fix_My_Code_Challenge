from flask import Blueprint, jsonify

app_views = Blueprint('app_views', __name__)


@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})

