from flask import Flask, jsonify
from flask import abort, make_response
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
from functions import get_all_tasks, get_task_by_id
from abc import ABC, abstractclassmethod



@app.route('/todo/tasks', methods=['GET'])
def get_tasks():
    return get_all_tasks()

@app.route('/todo/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    return get_task_by_id(task_id)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
