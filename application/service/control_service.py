from application.gateway.user_gateway import UserGateway
from application.gateway.log_gateway import LogGateway
from application.gateway.department_gateway import DepartmentGateway
from werkzeug.security import generate_password_hash
from jwt import decode
from application.settings import secret_key, algorithms
from application.visitor.visit_last_number import VisitorLastNumber


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
            #number = userDB.get_last_number()
            number = userDB.access_get_number(visitor=VisitorLastNumber)
            ControlService.write_to_log(usertoken,"user", str(number),"add")
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
    def user_edit_fields(usertoken, id_user, email, first_name, last_name, is_superuser):
        userDB = UserGateway(user_id=id_user, user_email=email, user_fn=first_name, user_sn=last_name, user_su=is_superuser)
        rv = userDB.update_fields()
        if rv['code']==0:
            ControlService.write_to_log(usertoken, "user", str(id_user), "edit")
        return rv

    @staticmethod
    def user_edit_password(usertoken, id_user, password):
        pw_hash = generate_password_hash(password)
        userDB = UserGateway(user_id=id_user, user_pass=pw_hash)
        rv = userDB.update_password()
        if rv['code']==0:
            ControlService.write_to_log(usertoken, "user", str(id_user), "edit_password")
        return rv

    @staticmethod
    def user_delete_by_id(usertoken, user_id):
        userDB = UserGateway(user_id=user_id)
        rv = userDB.delete()
        if rv['code']==0:
            ControlService.write_to_log(usertoken, "user", str(user_id), "delete")
        return rv

    @staticmethod
    def log_read_last(count):
        logDB = LogGateway()
        rv = logDB.read_last(count=count)
        if rv==None:
            return {}
        else:
            for (index, column) in enumerate(rv):
                tmp = column['date_time']
                rv[index]['date_time'] = tmp.strftime('%d.%m.%Y %H:%M')
        return rv

    @staticmethod
    def log_read_by_user(usertoken, count):
        logDB = LogGateway()
        identity = decode(usertoken, secret_key, algorithms)
        user_id = identity['identity']['id']
        rv = logDB.read_by_user_id(user_id=user_id, count=count)
        if rv==None:
            return {}
        else:
            for (index, column) in enumerate(rv):
                tmp = column['date_time']
                rv[index]['date_time'] = tmp.strftime('%d.%m.%Y %H:%M')
        return rv

    @staticmethod
    def department_add(usertoken, initials, caption):
        departmentDB = DepartmentGateway(department_initials=initials, department_name=caption)
        identity = decode(usertoken, secret_key, algorithms)
        user_id = identity['identity']['id']
        database_result = departmentDB.create()
        result = {
            "code": database_result['code'],
            "message": database_result['message'],
        }
        if result["code"]==0:
            number = departmentDB.access_get_number(visitor=VisitorLastNumber)
            ControlService.write_to_log(usertoken,"user", str(number),"add")
        return result


