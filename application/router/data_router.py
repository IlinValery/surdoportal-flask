from flask import make_response, jsonify
from application.service.viewer_service import ViewerService


class DataRouter:
    editor_service = ViewerService()

    @staticmethod
    def response_not_found(e):
        return make_response(jsonify({'error': 'Not found: 404'}), 404)

    @staticmethod
    def server_connection_test():
        return jsonify({"connection_status": "ОК"})

    def get_department_get_all(self):
        rv = self.editor_service.department_get_all()
        result = jsonify({"data": rv})
        return result


    def get_department_get_by_id(self, dep_id):
        rv = self.editor_service.department_get_by_id(dep_id)
        result = jsonify({"data": rv})
        return result

    def get_discipline_get_all(self):
        rv = self.editor_service.discipline_get_all()
        result = jsonify({"data": rv})
        return result


    def get_discipline_get_by_id(self, id):
        rv = self.editor_service.discipline_get_by_id(id)
        result = jsonify({"data": rv})
        return result


