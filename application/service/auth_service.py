from application.gateway.user_gateway import UserGateway
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash


class AuthService:

    @staticmethod
    def user_login(email, password):
        userDB = UserGateway()
        result = ""
        rv = userDB.read_by_email(email)
        if rv:
            if check_password_hash(rv['password'], password):
                access_token = create_access_token(identity= {"id": str(rv['iduser']), "first_name": rv['first_name'], "last_name": rv['last_name'], "email": rv['email'], "is_superuser": rv['is_superuser']})
                result = {"token": access_token}
            else:
                result = {"error": {"code": 2, "msg" : "Invalid password for user"}}
        else:
            result = {"error": {"code": 1, "msg": "No user with this email in system"}}
        return result
