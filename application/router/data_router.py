from flask import make_response, jsonify


class DataRouter:

    @staticmethod
    def response_not_found(e):
        return make_response(jsonify({'error': 'Not found: 404'}), 404)

    @staticmethod
    def server_connection_test():
        return jsonify({"connection_status": "ОК"})
