from application.application import Application
from flask_cors import CORS
from application.utils.create_superuser import create_superuser
from application.utils.create_database import create_tables, drop_all_tables

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
            application.server.run(debug=True, port=port)

        elif command == "createsuperuser":
            create_superuser()
        elif command == "createtables":
            create_tables()
        elif command == "droptables":
            drop_all_tables()
        else:
            print("Unsupported command! Use next commands:\n\t1. runserver\n\t2. createsuperuser\n\t3. createtables\n\t4. droptables")
