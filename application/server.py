from flask import Flask, jsonify, request, json
from flask_mysqldb import MySQL
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token

from flask import abort, make_response

from application.views import get_all_tasks, get_task_by_id


app = Flask(__name__)


cors = CORS(app)
mysql = MySQL(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)


def launch_server(port):
    app.config["MYSQL_USER"] = "surdo_user"
    app.config["MYSQL_PASSWORD"] = "UserPass123)"
    app.config["MYSQL_DB"] = "surdoDB"
    app.config["MYSQL_CURSORCLASS"] = "DictCursor"
    app.config["JWT_SECRET_KEY"] = "jmTVPowuEd4YPRbPMDySmfhXYuczUb4F"

    app.run(debug=True, port=port)


@app.route('/todo/tasks/', methods=['GET'])
def get_tasks():
    return get_all_tasks()

@app.route('/api/test_connection_with_server', methods=['GET'])
def server_connection_test():
    return jsonify({"connection_status": "ОК"})


@app.route('/todo/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    return get_task_by_id(task_id)


@app.route('/api/user/registration', methods=['POST'])
def user_registration():
    cursor = mysql.connection.cursor()
    email = str(request.get_json()["email"])
    first_name = str(request.get_json()['first_name'])
    second_name = str(request.get_json()['second_name'])
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf')
    is_superuser = int(request.get_json()['is_superuser'])

    cursor.execute("INSERT INTO users (email, first_name, second_name, password, is_superuser) VALUES ('"+
                   str(email) + "\', \'"+
                   str(first_name) + "\', \'"+
                   str(second_name) + "\', \'"+
                   str(password) + "\', \'"+
                   str(is_superuser) + "\');")
    mysql.connection.commit()

    result = {
        "email": email,
        "first_name": first_name,
        "last_name": second_name,
        "password": password,
        "is_super": is_superuser
    }
    return jsonify({"res":result})

# {
#   "email": "ivs@bmstu.ru",
#   "password": "herherher",
#   "first_name": "Valery",
#   "second_name": "Ilin",
#   "is_superuser": "1"
# }


@app.route('/api/user/login', methods=['POST'])
def user_login():
    print(request.get_json())
    cursor = mysql.connection.cursor()
    email = str(request.get_json()["email"])
    password = request.get_json()['password']

    result = ""

    cursor.execute("SELECT * FROM users where email = '"+str(email)+"'")

    rv = cursor.fetchone()
    if rv:
        if bcrypt.check_password_hash(rv['password'],password):
            access_token = create_access_token(identity= {"first_name": rv['first_name'], "second_name": rv['second_name'], "email": rv['email'], "is_superuser": rv['is_superuser']})
            result = jsonify({"token": access_token})
        else:
            result = jsonify({"error": {"code": 2, "msg" : "Invalid password for user"}})
    else:
        result = jsonify({"error": {"code": 1, "msg": "No user with this email in system"}})
    print(result)
    return result



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)





