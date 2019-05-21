from application.gateway.department_gateway import DepartmentGateway
from application.gateway.discipline_gateway import DisciplineGateway
from application.gateway.teacher_gateway import TeacherGateway
from application.gateway.media_gateway import MediaGateway
from application.gateway.term_gateway import TermGateway

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

    @staticmethod
    def term_get_count():
        term_db = TermGateway()
        rv = term_db.read_for_view()
        if rv==None:
            return 0
        else:
            return len(rv)

    @staticmethod
    def term_get_by_id(id):
        term_db = TermGateway()
        terms = term_db.read_by_id(id)
        teacher_db = TeacherGateway()
        teachers = teacher_db.read_all()
        if teachers==None:
            teachers = {}

        disciplines = {}
        department_db = DepartmentGateway()
        departments = department_db.read_all()
        if departments==None:
            departments = {}
        else:
            discipline_db = DisciplineGateway()
            disciplines = discipline_db.read_all()
            if disciplines==None:
                disciplines = {}
            else:
                for (index, row_discipline) in enumerate(disciplines):
                    department_id = row_discipline['department_id']
                    department = ''
                    for (index, row) in enumerate(departments):
                        if row['iddepartment']==department_id:
                            department = row['initials']
                    row_discipline['department_id'] = department


        if terms==None:
            return {"term": {}, "media": {}}
        else:
            media_db = MediaGateway()
            rv = media_db.read_by_term(id)
            if rv == None:
                rv = {}
            return {"term": terms, "media": rv, "disciplines": disciplines, "teachers": teachers}

    @staticmethod
    def term_get_filters():
        disciplines = {}
        department_db = DepartmentGateway()
        departments = department_db.read_all()
        if departments==None:
            departments = {}
        else:
            discipline_db = DisciplineGateway()
            disciplines = discipline_db.read_all()
            if disciplines==None:
                disciplines = {}
            else:
                for (index, row_discipline) in enumerate(disciplines):
                    department_id = row_discipline['department_id']
                    department = ''
                    for (index, row) in enumerate(departments):
                        if row['iddepartment']==department_id:
                            department = row
                    row_discipline['department_id'] = department


        return {"departments": departments, "disciplines": disciplines}

    @staticmethod
    def term_view(discipline_id, phrase):
        on_page = 80
        start = 0
        end = on_page
        term_db = TermGateway()
        rv = term_db.read_for_view(start, end, discipline_id, phrase)
        if rv==None:
            return {}
        else:
            return rv

