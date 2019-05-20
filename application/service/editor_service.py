from application.gateway.term_gateway import TermGateway
from application.gateway.media_gateway import MediaGateway
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
    def term_edit_by_id(usertoken, term_id,  caption, description, discipline, teacher, creator, lesson, image_path, is_shown = 0):
        term_db = TermGateway(term_id=term_id, term_caption=caption, term_description=description, term_discipline=discipline,
                              term_teacher=teacher, term_creator=creator, term_lesson=lesson, term_image=image_path,
                              term_is_shown=is_shown)
        rv = term_db.update()
        if rv['code'] == 0:
            ControlService.write_to_log(usertoken, "term", str(term_id), "edit")
        return rv

    @staticmethod
    def media_add(usertoken, type, youtube_id, term_id):
        media_db = MediaGateway(media_type=type, media_youtube_id=youtube_id, media_to_term=term_id)
        database_result = media_db.create()
        result = {
            "code": database_result['code'],
            "message": database_result['message'],
        }
        if result["code"] == 0:
            number = media_db.access_get_number(visitor=VisitorLastNumber)
            ControlService.write_to_log(usertoken, "media", str(number), "add")
        return result

    @staticmethod
    def media_delete_by_id(usertoken, media_id):
        media_db = MediaGateway(media_id=media_id)
        rv = media_db.delete()
        if rv['code'] == 0:
            ControlService.write_to_log(usertoken, "media", str(media_id), "delete")
        return rv

    @staticmethod
    def media_edit_by_id(usertoken, media_id, type, youtube_id, term_id):
        media_db = MediaGateway(media_id=media_id, media_type=type, media_youtube_id=youtube_id, media_to_term=term_id)
        rv = media_db.update()
        if rv['code'] == 0:
            ControlService.write_to_log(usertoken, "media", str(media_id), "edit")
        return rv

    #todo by params
    @staticmethod
    def teacher_get_by_params(page=0, only_invalided=0, discipline_id=0, user_id=0):
        on_page = 40
        start = on_page*(page-1)
        end = start+on_page
        term_db = TermGateway()
        rv = term_db.read_for_editor(start,end,only_invalided,discipline_id,user_id)
        if rv==None:
            return {}
        else:
            return rv

