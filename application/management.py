from application.application import Application
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from application.utils.create_superuser import create_superuser


def execute_from_terminal(args):

    if len(args) == 1:
        print("No parameters here! \nFor start this app use script\n\tpython startapp.py runserver")
        return -1
    else:
        command = args[1]
        if command == "runserver":
            port = 5555
            application = Application(port=port)
            cors = CORS(application.server)
            jwt = JWTManager(application.server)
            application.create_app()
            application.server.run(debug=True, port=port)

        elif command == "createsuperuser":
            create_superuser()
        else:
            print("Unsupported command! Use next commands:\n\t1. runserver\n\t2. createsuperuser")
