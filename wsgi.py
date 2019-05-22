from application.application import Application
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

application = Application(port=5555)
cors = CORS(application.server)

application.server.wsgi_app = ProxyFix(application.server.wsgi_app)
if __name__ == '__main__':
    application.create_app()
    application.server.run(debug=True, port=5555)

