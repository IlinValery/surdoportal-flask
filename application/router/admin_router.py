from flask import make_response, jsonify, request
from flask_jwt_extended import get_jwt_identity

from application.service.auth_service import AuthService
from application.service.control_service import ControlService
from application.service.editor_service import EditorService


class AdminRouter():
    auth_service = AuthService()
    control_service = ControlService()
    editor_service = EditorService()

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

    def post_log_read_by_user(self):
        usertoken = request.get_json()["usertoken"]
        count = request.get_json()["count"]
        rv = self.control_service.log_read_by_user(usertoken, count)
        result = jsonify({"data": rv})
        return result

    def post_department_add(self):
        usertoken = str(request.get_json()['usertoken'])
        initials = str(request.get_json()['initials'])
        caption = str(request.get_json()['caption'])
        result = self.control_service.department_add(usertoken, initials=initials, caption=caption)
        return jsonify({"result": result})

    def post_department_delete_by_id(self):
        department_id = str(request.get_json()["department_id"])
        usertoken = str(request.get_json()["usertoken"])
        rv = self.control_service.department_delete_by_id(usertoken, department_id)
        result = jsonify({"result": rv})
        return result

    def post_department_edit_by_id(self):
        department_id = str(request.get_json()["department_id"])
        initials = str(request.get_json()["initials"])
        caption = str(request.get_json()["caption"])
        usertoken = str(request.get_json()["usertoken"])
        rv = self.control_service.department_edit_by_id(usertoken, department_id, initials, caption)
        result = jsonify({"result": rv})
        return result

    def post_discipline_add(self):
        usertoken = str(request.get_json()['usertoken'])
        name = str(request.get_json()['name'])
        semester = int(request.get_json()['semester'])
        department_id = int(request.get_json()['department_id'])
        result = self.control_service.discipline_add(usertoken=usertoken, name=name, semester=semester, department_id=department_id)
        return jsonify({"result": result})

    def post_discipline_delete_by_id(self):
        discipline_id = int(request.get_json()["discipline_id"])
        usertoken = str(request.get_json()["usertoken"])
        rv = self.control_service.discipline_delete_by_id(usertoken, discipline_id)
        result = jsonify({"result": rv})
        return result

    def post_discipline_edit_by_id(self):
        discipline_id = str(request.get_json()["discipline_id"])
        usertoken = str(request.get_json()['usertoken'])
        name = str(request.get_json()['name'])
        semester = int(request.get_json()['semester'])
        department_id = int(request.get_json()['department_id'])
        rv = self.control_service.discipline_edit_by_id(usertoken=usertoken, discipline_id=discipline_id, name=name, semester=semester, department_id=department_id)
        result = jsonify({"result": rv})
        return result

    def post_teacher_add(self):
        usertoken = str(request.get_json()['usertoken'])
        name = str(request.get_json()['name'])
        department_id = int(request.get_json()['department_id'])
        result = self.control_service.teacher_add(usertoken=usertoken, name=name, department_id=department_id)
        return jsonify({"result": result})

    def post_teacher_delete_by_id(self):
        teacher_id = int(request.get_json()["teacher_id"])
        usertoken = str(request.get_json()["usertoken"])
        rv = self.control_service.teacher_delete_by_id(usertoken, teacher_id)
        result = jsonify({"result": rv})
        return result

    def post_teacher_edit_by_id(self):
        teacher_id = str(request.get_json()["teacher_id"])
        usertoken = str(request.get_json()['usertoken'])
        name = str(request.get_json()['name'])
        department_id = int(request.get_json()['department_id'])
        rv = self.control_service.teacher_edit_by_id(usertoken=usertoken, teacher_id=teacher_id, name=name, department_id=department_id)
        result = jsonify({"result": rv})
        return result

    def get_disciplines_users(self):
        result = self.editor_service.disciplines_users_for_term_editor()
        return jsonify({"result": result})

    def post_term_add(self):
        usertoken = str(request.get_json()['usertoken'])
        caption = str(request.get_json()['caption'])
        description = str(request.get_json()['description'])
        discipline_id = int(request.get_json()['discipline_id'])
        teacher_id = int(request.get_json()['teacher_id'])
        lesson = int(request.get_json()['lesson'])
        image_path = str(request.get_json()['image_path'])
        result = self.editor_service.term_add(usertoken=usertoken, caption=caption, description=description,
                                              discipline=discipline_id, teacher=teacher_id,
                                              lesson=lesson, image_path=image_path)
        return jsonify({"result": result})




    def post_term_view(self):
        user_id = int(request.get_json()["creator_id"])
        discipline_id = int(request.get_json()["discipline_id"])
        only_invalided = int(request.get_json()["only_invalided"])
        page = int(request.get_json()["page"])
        rv = self.editor_service.term_get_by_params(page, only_invalided, discipline_id, user_id)

        result = jsonify({"result": rv})
        return result




    #TODO
    def post_term_delete_by_id(self):
        teacher_id = int(request.get_json()["teacher_id"])
        usertoken = str(request.get_json()["usertoken"])
        rv = self.control_service.teacher_delete_by_id(usertoken, teacher_id)
        result = jsonify({"result": rv})
        return result

    def post_term_edit_by_id(self):
        teacher_id = str(request.get_json()["teacher_id"])
        usertoken = str(request.get_json()['usertoken'])
        name = str(request.get_json()['name'])
        department_id = int(request.get_json()['department_id'])
        rv = self.control_service.teacher_edit_by_id(usertoken=usertoken, teacher_id=teacher_id, name=name, department_id=department_id)
        result = jsonify({"result": rv})
        return result

    def post_term_validate_by_id(self):
        teacher_id = str(request.get_json()["teacher_id"])
        usertoken = str(request.get_json()['usertoken'])
        name = str(request.get_json()['name'])
        department_id = int(request.get_json()['department_id'])
        rv = self.control_service.teacher_edit_by_id(usertoken=usertoken, teacher_id=teacher_id, name=name, department_id=department_id)
        result = jsonify({"result": rv})
        return result


    def post_media_add(self):
        usertoken = str(request.get_json()['usertoken'])
        name = str(request.get_json()['name'])
        department_id = int(request.get_json()['department_id'])
        result = self.control_service.teacher_add(usertoken=usertoken, name=name, department_id=department_id)
        return jsonify({"result": result})

    def post_media_delete_by_id(self):
        teacher_id = int(request.get_json()["teacher_id"])
        usertoken = str(request.get_json()["usertoken"])
        rv = self.control_service.teacher_delete_by_id(usertoken, teacher_id)
        result = jsonify({"result": rv})
        return result

    def post_media_edit_by_id(self):
        teacher_id = str(request.get_json()["teacher_id"])
        usertoken = str(request.get_json()['usertoken'])
        name = str(request.get_json()['name'])
        department_id = int(request.get_json()['department_id'])
        rv = self.control_service.teacher_edit_by_id(usertoken=usertoken, teacher_id=teacher_id, name=name, department_id=department_id)
        result = jsonify({"result": rv})
        return result
