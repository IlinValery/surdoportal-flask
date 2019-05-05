from application.settings import app, bcrypt
from flask_jwt_extended import create_access_token
from flask import abort, make_response
from flask import jsonify, request

from application.views import get_all_tasks, get_task_by_id

from table_data_gateway.user_gateway import UserGateway

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
    email = str(request.get_json()["email"])
    first_name = str(request.get_json()['first_name'])
    second_name = str(request.get_json()['second_name'])
    password = str(request.get_json()['password'])
    is_superuser = int(request.get_json()['is_superuser'])

    user = UserGateway(user_email=email, user_fn=first_name, user_sn=second_name, user_pass=password,user_su=is_superuser)

    user.create()



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
    email = str(request.get_json()["email"])
    password = request.get_json()['password']
    user = UserGateway(user_email=email)
    result = ""
    res = user.read(by_email=True)
    print(res)
    # cursor.execute("SELECT * FROM users where email = '"+str(email)+"'")
    #
    # rv = cursor.fetchone()
    rv = user.read(by_email=True)
    if rv:
        if bcrypt.check_password_hash(rv['password'],password):
            access_token = create_access_token(identity= {"first_name": rv['first_name'], "second_name": rv['second_name'], "email": rv['email'], "is_superuser": rv['is_superuser']})
            print(access_token)
            result = jsonify({"token": access_token})
        else:
            result = jsonify({"error": {"code": 2, "msg" : "Invalid password for user"}})
    else:
        result = jsonify({"error": {"code": 1, "msg": "No user with this email in system"}})
    print("!!!!!!!!!!!!!!!!!!!!!!", result)
    return result



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)





