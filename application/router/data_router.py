from application.service.viewer_service import ViewerService
from flask import make_response, jsonify, request


class DataRouter:
    viewer_service = ViewerService()
    
    @staticmethod
    def response_not_found(e):
        return make_response(jsonify({'error': 'Not found: 404'}), 404)

    @staticmethod
    def server_connection_test():
        return jsonify({"connection_status": "ОК"})

    def get_department_get_all(self):
        rv = self.viewer_service.department_get_all()
        result = jsonify({"data": rv})
        return result


    def get_department_get_by_id(self, dep_id):
        rv = self.viewer_service.department_get_by_id(dep_id)
        result = jsonify({"data": rv})
        return result

    def get_discipline_get_all(self):
        rv = self.viewer_service.discipline_get_all()
        result = jsonify({"data": rv})
        return result


    def get_discipline_get_by_id(self, id):
        rv = self.viewer_service.discipline_get_by_id(id)
        result = jsonify({"data": rv})
        return result

    def get_teacher_get_all(self):
        rv = self.viewer_service.teacher_get_all()
        result = jsonify({"data": rv})
        return result


    def get_teacher_get_by_id(self, id):
        rv = self.viewer_service.teacher_get_by_id(id)
        result = jsonify({"data": rv})
        return result

    def get_term_count(self):
        rv = self.viewer_service.term_get_count()
        result = jsonify({"count_terms": rv})
        return result

    def get_term_get_by_id(self, id):
        rv = self.viewer_service.term_get_by_id(id)
        result = jsonify({"data": rv})
        return result

    def get_term_random(self):
        rv = self.viewer_service.term_get_random()
        result = jsonify({"data": rv})
        return result


    def get_terms_params(self):
        rv = self.viewer_service.term_get_filters()
        result = jsonify({"data": rv})
        return result

    def post_term_get_by_params(self):
        discipline_id = int(request.get_json()["discipline_id"])
        phrase = str(request.get_json()["phrase"])
        rv = self.viewer_service.term_view(discipline_id, phrase)
        result = jsonify({"data": rv})
        return result

