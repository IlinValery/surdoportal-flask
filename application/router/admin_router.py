from flask import make_response, jsonify, request
from flask_jwt_extended import get_jwt_identity

from application.service.auth_service import AuthService
from application.service.control_service import ControlService


class AdminRouter():
    auth_service = AuthService()
    control_service = ControlService()

    def post_user_login(self):
        email = str(request.get_json()["email"])
        password = request.get_json()['password']
        result = self.auth_service.user_login(email, password)
        return jsonify(result)

    def post_user_register(self):
        email = str(request.get_json()["email"])
        first_name = str(request.get_json()['first_name'])
        last_name = str(request.get_json()['last_name'])
        password = str(request.get_json()['password'])
        is_superuser = int(request.get_json()['is_superuser'])
        usertoken = str(request.get_json()['usertoken'])
        result = self.control_service.user_register(usertoken, email, first_name, last_name, password, is_superuser)
        return jsonify({"result": result})

    def get_user_get_all(self):
        rv = self.control_service.user_get_all()
        result = jsonify({"data": rv})
        return result

    def get_user_by_id(self, user_id):
        rv = self.control_service.user_by_id(user_id)
        result = jsonify({"data": rv})
        return result

    def post_user_edit_fields(self):
        id_user = str(request.get_json()["id"])
        email = str(request.get_json()["email"])
        first_name = str(request.get_json()['first_name'])
        last_name = str(request.get_json()['last_name'])
        is_superuser = int(request.get_json()['is_superuser'])
        usertoken = str(request.get_json()["usertoken"])
        rv = self.control_service.user_edit_fields(usertoken, id_user, email, first_name, last_name, is_superuser)
        result = jsonify({"result": rv})
        return result

    def post_user_edit_password(self):
        id_user = str(request.get_json()["id"])
        password = str(request.get_json()["password"])
        usertoken = str(request.get_json()["usertoken"])
        rv = self.control_service.user_edit_password(usertoken, id_user, password)
        result = jsonify({"result": rv})
        return result

    def post_user_delete_by_id(self):
        user_id = str(request.get_json()["user_id"])
        usertoken = str(request.get_json()["usertoken"])
        rv = self.control_service.user_delete_by_id(usertoken, user_id)
        result = jsonify({"data": rv})
        return result

    def post_log_read_last(self):
        count = request.get_json()["count"]
        rv = self.control_service.log_read_last(count)
        result = jsonify({"data": rv})
        return result


