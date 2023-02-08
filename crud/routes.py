from crud import app
from flask import jsonify, request

from crud.database import Database
from crud.singleton import Logging

db_obj = Database()
# db_obj.create_conn()
# Singleton import

log_obj = Logging()
log_obj.set_log_level("API", 'DEBUG')
logger = log_obj.get_logger('API')

@app.route('/')
def index():
    logger.info('API is running')
    return jsonify({
            'status': 'Success',
            'message': 'API is running'
        }), 200

@app.route('/get_items', methods=['GET'])
def get_items():
    if request.method == 'GET':
        try:
            return jsonify({
                'status': 'Success',
                'message': 'List of Products',
                'products': db_obj.get_items()
            }), 200

        except Exception as exc:
            logger.error(exc)
            return jsonify({
                'status': 'Error',
                'message': 'Product could not be added.'
            }), 500
    return db_obj.get_items()

@app.route('/add_item', methods=['POST'])
def add_item():
    if request.method == 'POST':
        try:
            name = request.json.get("name")
            description = request.json.get("description")
            
            db_obj.add_item(name, description)
            return jsonify({
                'status': 'Success',
                'message': 'Product added sucessfully'
            }), 200

        except Exception as exc:
            logger.error(exc)
            return jsonify({
                'status': 'Error',
                'message': 'Product could not be added.'
            }), 500


@app.route('/update_item', methods=['POST'])
def update_item():
    if request.method == 'POST':
        try:
            name = request.json.get("name")
            description = request.json.get("description")
            id = request.json.get("id")

            db_obj.update_item(name, description, id)
            return jsonify({
                'status': 'Success',
                'message': 'Product updated sucessfully'
            }), 200

        except Exception as e:
            logger.error(e)
            return jsonify({
                'status': 'Error',
                'message': 'Product could not be updated.'
            }), 500

@app.route('/delete_item', methods=['POST'])
def delete_item():
    if request.method == 'POST':
        try:
            id = request.json.get("id")

            db_obj.delete_item(id)
            return jsonify({
                'status': 'Success',
                'message': 'Product deleted sucessfully'
            }), 200

        except Exception as e:
            logger.error(e)
            return jsonify({
                'status': 'Error',
                'message': 'Product could not be deleted.'
            }), 500
        db_obj.delete_item(id)
    