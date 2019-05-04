from application.server import launch_server

def execute_from_terminal(args):
    if len(args) == 1:
        print("No parameters here! \nFor start this app use script\n\tpython startapp.py runserver <port (default 5555)>")
        return -1
    else:
        command = args[1]
        param = ""
        if len(args) > 2:
            param = args[2]
        if command == "runserver":
            port = 5555
            if param != "":
                port = int(param)

            launch_server(port)

