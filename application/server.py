from application.settings import app, bcrypt
from flask_jwt_extended import create_access_token
from flask import abort, make_response
from flask import jsonify, request

from application.views import get_all_tasks, get_task_by_id

from table_data_gateway.user_gateway import UserGateway
from table_data_gateway.log_gateway import LogGateway


@app.route('/api/test_connection_with_server', methods=['GET'])
def server_connection_test():
    return jsonify({"connection_status": "ОК"})


@app.route('/api/user/create', methods=['POST'])
def post_user_create():
    email = str(request.get_json()["email"])
    first_name = str(request.get_json()['first_name'])
    last_name = str(request.get_json()['last_name'])
    password = str(request.get_json()['password'])
    is_superuser = int(request.get_json()['is_superuser'])

    userDB = UserGateway(user_email=email, user_fn=first_name, user_sn=last_name, user_pass=password,user_su=is_superuser)

    database_result = userDB.create()

    result = {
        "code": database_result['code'],
        "message": database_result['message'],
    }
    return jsonify({"result" : result})



@app.route('/api/user/login', methods=['POST'])
def user_login():
    email = str(request.get_json()["email"])
    password = request.get_json()['password']
    userDB = UserGateway()
    result = ""

    rv = userDB.read_by_email(email)
    if rv:
        if bcrypt.check_password_hash(rv['password'],password):
            access_token = create_access_token(identity= {"id": str(rv['iduser']), "first_name": rv['first_name'], "last_name": rv['last_name'], "email": rv['email'], "is_superuser": rv['is_superuser']})
            result = jsonify({"token": access_token})
        else:
            result = jsonify({"error": {"code": 2, "msg" : "Invalid password for user"}})
    else:
        result = jsonify({"error": {"code": 1, "msg": "No user with this email in system"}})
    return result


@app.route('/api/user/all', methods=['GET'])
def user_get_all():
    userDB = UserGateway()
    result = ""
    rv = userDB.read_all()
    result = jsonify({"data": rv})
    return result


@app.route('/api/user/<int:user_id>', methods=['GET'])
def user_get_by_id(user_id):
    userDB = UserGateway()
    result = ""
    rv = userDB.read_by_id(user_id)
    result = jsonify({"data": rv})
    return result


@app.route('/api/user/edit_fields', methods=['POST'])
def user_edit_fields():
    id_user = str(request.get_json()["id"])
    email = str(request.get_json()["email"])
    first_name = str(request.get_json()['first_name'])
    last_name = str(request.get_json()['last_name'])
    is_superuser = int(request.get_json()['is_superuser'])
    userDB = UserGateway(user_id=id_user, user_email=email, user_fn=first_name, user_sn=last_name, user_su=is_superuser)
    rv = userDB.update_fields()
    result = jsonify({"result": rv})
    return result

@app.route('/api/user/edit_password', methods=['POST'])
def user_edit_password():
    id_user = str(request.get_json()["id"])
    password = str(request.get_json()["password"])
    userDB = UserGateway(user_id=id_user, user_pass=password)
    rv = userDB.update_password()
    result = jsonify({"result": rv})
    return result



@app.route('/api/user/delete', methods=['POST'])
def user_delete_by_id():
    user_id = str(request.get_json()["user_id"])
    userDB = UserGateway(user_id=user_id)
    result = ""
    rv = userDB.delete()
    result = jsonify({"data": rv})
    return result


@app.route('/api/log/read_all/<int:count>', methods=['GET'])
def get_log_count(count):
    logDB = LogGateway()
    result = ""
    rv = logDB.read_last(count)
    result = jsonify({"data": rv})
    return result



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)





