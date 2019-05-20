from application.gateway.user_gateway import UserGateway
from application.gateway.log_gateway import LogGateway
from application.gateway.department_gateway import DepartmentGateway
from application.gateway.discipline_gateway import DisciplineGateway
from application.gateway.teacher_gateway import TeacherGateway
from application.gateway.term_gateway import TermGateway
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
        user_db = UserGateway(user_email=email, user_fn=first_name, user_sn=last_name, user_pass=pw_hash,
                             user_su=is_superuser)

        database_result = user_db.create()
        result = {
            "code": database_result['code'],
            "message": database_result['message'],
        }
        if result["code"]==0:
            #number = user_db.get_last_number()
            number = user_db.access_get_number(visitor=VisitorLastNumber)
            ControlService.write_to_log(usertoken,"user", str(number),"add")
        return result

    @staticmethod
    def user_get_all():
        user_db = UserGateway()
        rv = user_db.read_all()
        return rv

    @staticmethod
    def user_by_id(user_id):
        user_db = UserGateway()
        rv = user_db.read_by_id(user_id)
        return rv

    @staticmethod
    def user_edit_fields(usertoken, id_user, email, first_name, last_name, is_superuser):
        user_db = UserGateway(user_id=id_user, user_email=email, user_fn=first_name, user_sn=last_name, user_su=is_superuser)
        rv = user_db.update_fields()
        if rv['code']==0:
            ControlService.write_to_log(usertoken, "user", str(id_user), "edit")
        return rv

    @staticmethod
    def user_edit_password(usertoken, id_user, password):
        pw_hash = generate_password_hash(password)
        user_db = UserGateway(user_id=id_user, user_pass=pw_hash)
        rv = user_db.update_password()
        if rv['code']==0:
            ControlService.write_to_log(usertoken, "user", str(id_user), "edit_password")
        return rv

    @staticmethod
    def user_delete_by_id(usertoken, user_id):
        user_db = UserGateway(user_id=user_id)
        rv = user_db.delete()
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
        depatment_db = DepartmentGateway(department_initials=initials, department_name=caption)
        identity = decode(usertoken, secret_key, algorithms)
        database_result = depatment_db.create()
        result = {
            "code": database_result['code'],
            "message": database_result['message'],
        }
        if result["code"] == 0:
            number = depatment_db.access_get_number(visitor=VisitorLastNumber)
            print(number)
            ControlService.write_to_log(usertoken, "department", str(number),"add")
        return result

    @staticmethod
    def department_delete_by_id(usertoken, department_id):
        depatment_db = DepartmentGateway(department_id=department_id)
        rv = depatment_db.delete()
        if rv['code'] == 0:
            ControlService.write_to_log(usertoken, "department", str(department_id), "delete")
        return rv

    @staticmethod
    def department_edit_by_id(usertoken, department_id, initials, caption):
        depatment_db = DepartmentGateway(department_id=department_id, department_initials=initials, department_name=caption)
        rv = depatment_db.update()
        if rv['code'] == 0:
            ControlService.write_to_log(usertoken, "department", str(department_id), "edit")
        return rv

    @staticmethod
    def discipline_add(usertoken, name, semester, department_id):
        discipline_db = DisciplineGateway(discipline_name=name, discipline_semester=semester, discipline_to_department=department_id)
        database_result = discipline_db.create()
        result = {
            "code": database_result['code'],
            "message": database_result['message'],
        }
        if result["code"] == 0:
            number = discipline_db.access_get_number(visitor=VisitorLastNumber)
            ControlService.write_to_log(usertoken, "discipline", str(number),"add")
        return result

    @staticmethod
    def discipline_delete_by_id(usertoken, discipline_id):
        discipline_db = DisciplineGateway(discipline_id=discipline_id)
        rv = discipline_db.delete()
        if rv['code'] == 0:
            ControlService.write_to_log(usertoken, "discipline", str(discipline_id), "delete")
        return rv

    @staticmethod
    def discipline_edit_by_id(usertoken, discipline_id, name, semester, department_id):
        discipline_db = DisciplineGateway(discipline_id=discipline_id, discipline_name=name, discipline_semester=semester, discipline_to_department=department_id)
        rv = discipline_db.update()
        if rv['code'] == 0:
            ControlService.write_to_log(usertoken, "discipline", str(discipline_id), "edit")
        return rv

    @staticmethod
    def teacher_add(usertoken, name, department_id):
        teacher_db = TeacherGateway(teacher_name=name, teacher_to_department=department_id)
        database_result = teacher_db.create()
        result = {
            "code": database_result['code'],
            "message": database_result['message'],
        }
        if result["code"] == 0:
            number = teacher_db.access_get_number(visitor=VisitorLastNumber)
            ControlService.write_to_log(usertoken, "teacher", str(number),"add")
        return result

    @staticmethod
    def teacher_delete_by_id(usertoken, teacher_id):
        teacher_db = TeacherGateway(teacher_id=teacher_id)
        rv = teacher_db.delete()
        if rv['code'] == 0:
            ControlService.write_to_log(usertoken, "teacher", str(teacher_id), "delete")
        return rv

    @staticmethod
    def teacher_edit_by_id(usertoken, teacher_id, name, department_id):
        teacher_db = TeacherGateway(teacher_id=teacher_id, teacher_name=name, teacher_to_department=department_id)
        rv = teacher_db.update()
        if rv['code'] == 0:
            ControlService.write_to_log(usertoken, "teacher", str(teacher_id), "edit")
        return rv

    @staticmethod
    def term_delete_by_id(usertoken, term_id):
        term_db = TermGateway(term_id=term_id)
        rv = term_db.delete()
        if rv['code'] == 0:
            ControlService.write_to_log(usertoken, "term", str(term_id), "delete")
        return rv

