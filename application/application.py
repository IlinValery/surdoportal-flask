from flask import Flask
from application.router.data_router import DataRouter
from application.router.admin_router import AdminRouter

secret_key = "jmTVPowuEd4YPRbPMDySmfhXYuczUb4F"

class Application:
    def __init__(self, port):
        self.port=port
        self.server = Flask(__name__)

    def create_app(self) -> None:
        data_router = DataRouter()
        admin_router = AdminRouter()

        with self.server.app_context():

            self.server.config["JWT_SECRET_KEY"] = secret_key

            self.server.register_error_handler(404, data_router.response_not_found)
            self.server.add_url_rule('/api/test_connection_with_server', view_func=data_router.server_connection_test, methods=['GET'])

            self.server.add_url_rule('/api/user/login', view_func=admin_router.post_user_login, methods=['POST'])

            #user_control
            self.server.add_url_rule('/api/user/create', view_func=admin_router.post_user_register, methods=['POST'])
            self.server.add_url_rule('/api/user/all', view_func=admin_router.get_user_get_all, methods=['GET'])
            self.server.add_url_rule('/api/user/<int:user_id>', view_func=admin_router.get_user_by_id, methods=['GET'])
            self.server.add_url_rule('/api/user/edit_fields', view_func=admin_router.post_user_edit_fields, methods=['POST'])
            self.server.add_url_rule('/api/user/edit_password', view_func=admin_router.post_user_edit_password, methods=['POST'])
            self.server.add_url_rule('/api/user/delete', view_func=admin_router.post_user_delete_by_id, methods=['POST'])

            self.server.add_url_rule('/api/log/read_all', view_func=admin_router.post_log_read_last, methods=['POST'])
            self.server.add_url_rule('/api/log/read_by_user', view_func=admin_router.post_log_read_by_user, methods=['POST'])


            self.server.add_url_rule('/api/department/create', view_func=admin_router.post_department_add, methods=['POST'])

            self.server.add_url_rule('/api/department/all', view_func=data_router.get_department_get_all, methods=['GET'])
            self.server.add_url_rule('/api/department/<int:dep_id>', view_func=data_router.get_department_get_by_id, methods=['GET'])
            self.server.add_url_rule('/api/department/edit', view_func=admin_router.post_department_edit_by_id, methods=['POST'])
            self.server.add_url_rule('/api/department/delete', view_func=admin_router.post_department_delete_by_id, methods=['POST'])
