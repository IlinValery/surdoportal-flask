from application.gateway.term_gateway import TermGateway
from application.service.control_service import ControlService
from application.visitor.visit_last_number import VisitorLastNumber

class EditorService:

    @staticmethod
    def term_add(usertoken, caption, description, discipline, teacher, creator, lesson, image_path, is_shown = 0):
        term_db = TermGateway(term_caption=caption, term_description=description, term_discipline=discipline,
                              term_teacher=teacher, term_creator=creator, term_lesson=lesson, term_image=image_path,
                              term_is_shown=is_shown)
        database_result = term_db.create()
        result = {
            "code": database_result['code'],
            "message": database_result['message'],
        }
        if result["code"] == 0:
            number = term_db.access_get_number(visitor=VisitorLastNumber)
            ControlService.write_to_log(usertoken, "term", str(number),"add")
        return result

    @staticmethod
    def term_delete_by_id(usertoken, term_id):
        term_db = TermGateway(term_id=term_id)
        rv = term_db.delete()
        if rv['code'] == 0:
            ControlService.write_to_log(usertoken, "term", str(term_id), "delete")
        return rv

    # @staticmethod
    # def term_edit_by_id(usertoken, term_id, name, department_id):
    #     term_db = TermGateway(teacher_id=teacher_id, teacher_name=name, teacher_to_department=department_id)
    #     rv = term_db.update()
    #     if rv['code'] == 0:
    #         ControlService.write_to_log(usertoken, "teacher", str(teacher_id), "edit")
    #     return rv


    @staticmethod
    def teacher_get_by_params():
        term_db = TermGateway()
        rv = term_db.read_for_editor()
        if rv==None:
            return {}
        else:
            return rv

