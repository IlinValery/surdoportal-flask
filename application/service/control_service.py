from application.gateway.user_gateway import UserGateway
from application.gateway.log_gateway import LogGateway
from werkzeug.security import generate_password_hash
from jwt import decode
from application.settings import secret_key, algorithms

class ControlService:
    """
    Класс для управления данными (пользователи, кафедры, преподаватели, дисциплины) - удаление, добавление, изменение
    """

    @staticmethod
    def write_to_log(usertoken, table, element_id, action):
        identity = decode(usertoken, secret_key, algorithms)
        user_id = identity['identity']['id']
        log = LogGateway(log_user_id=user_id, log_table=table, log_element_id=element_id, log_action=action).create()
        pass


    @staticmethod
    def user_register(usertoken, email, first_name, last_name, password, is_superuser):
        pw_hash = generate_password_hash(password)
        userDB = UserGateway(user_email=email, user_fn=first_name, user_sn=last_name, user_pass=pw_hash,
                             user_su=is_superuser)

        database_result = userDB.create()

        result = {
            "code": database_result['code'],
            "message": database_result['message'],
        }
        if result["code"]==0:
            ControlService.write_to_log(usertoken,"user", "1","add")
        return result

    @staticmethod
    def user_get_all():
        userDB = UserGateway()
        rv = userDB.read_all()
        return rv

    @staticmethod
    def user_by_id(user_id):
        userDB = UserGateway()
        rv = userDB.read_by_id(user_id)
        return rv

    @staticmethod
    def user_edit_fields(id_user, email, first_name, last_name, is_superuser):
        userDB = UserGateway(user_id=id_user, user_email=email, user_fn=first_name, user_sn=last_name, user_su=is_superuser)
        rv = userDB.update_fields()
        return rv

    @staticmethod
    def user_edit_password(id_user, password):
        pw_hash = generate_password_hash(password)
        userDB = UserGateway(user_id=id_user, user_pass=pw_hash)
        rv = userDB.update_password()
        return rv

    @staticmethod
    def user_delete_by_id(user_id):
        userDB = UserGateway(user_id=user_id)
        rv = userDB.delete()
        return rv

    @staticmethod
    def log_read_last(count):
        logDB = LogGateway()
        rv = logDB.read_last(count=count)
        if rv==None:
            return {}
        return rv


