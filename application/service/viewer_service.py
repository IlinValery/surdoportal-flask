from application.gateway.department_gateway import DepartmentGateway
from application.gateway.discipline_gateway import DisciplineGateway
from application.gateway.teacher_gateway import TeacherGateway

class ViewerService:

    @staticmethod
    def department_get_all():
        department_db = DepartmentGateway()
        rv = department_db.read_all()
        if rv==None:
            return {}
        else:
            return rv

    @staticmethod
    def department_get_by_id(dep_id):
        department_db = DepartmentGateway()
        rv = department_db.read_by_id(dep_id)
        return rv

    @staticmethod
    def discipline_get_all():
        discipline_db = DisciplineGateway()
        rv = discipline_db.read_all()
        if rv==None:
            return {}
        else:
            return rv

    @staticmethod
    def discipline_get_by_id(id):
        discipline_db = DisciplineGateway()
        rv = discipline_db.read_by_id(id)
        return rv

    @staticmethod
    def teacher_get_all():
        teacher_db = TeacherGateway()
        rv = teacher_db.read_all()
        if rv==None:
            return {}
        else:
            return rv

    @staticmethod
    def teacher_get_by_id(id):
        teacher_db = TeacherGateway()
        rv = teacher_db.read_by_id(id)
        return rv


