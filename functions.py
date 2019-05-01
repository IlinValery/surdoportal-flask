from flask import Flask, jsonify

from flask import abort, make_response
from data import tasks

def get_all_tasks():
    return jsonify({'data': tasks})

def get_task_by_id(task_id):
    print(task_id)
    task = []
    for t in tasks:
        if t['id']==task_id:
            task.append(t)
    print(task)
    if len(task) == 0:
        abort(404)
    return jsonify({'data': task[0]})
