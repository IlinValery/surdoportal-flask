from application.gateway.user_gateway import UserGateway
from werkzeug.security import check_password_hash
from jwt import encode
from application.settings import secret_key, algorithms

class AuthService:

    @staticmethod
    def user_login(email, password):
        userDB = UserGateway()
        result = ""
        rv = userDB.read_by_email(email)
        if rv:
            if check_password_hash(rv['password'], password):
                identity = {"id": str(rv['iduser']), "first_name": rv['first_name'], "last_name": rv['last_name'],
                            "email": rv['email'], "is_superuser": rv['is_superuser']}

                access_token = encode({"identity":identity}, secret_key, algorithms)
                result = {"token": access_token.decode('utf-8')}
            else:
                result = {"error": {"code": 2, "msg" : "Invalid password for user"}}
        else:
            result = {"error": {"code": 1, "msg": "No user with this email in system"}}
        return result
