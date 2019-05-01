#!flask/bin/python
from flask import Flask, jsonify

from flask import abort, make_response


app = Flask(__name__)
from functions import get_tasks, get_task



@app.route('/todo/tasks', methods=['GET'])
def get_tasks():
    pass

@app.route('/todo/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    pass

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)