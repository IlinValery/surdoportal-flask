from application.gateway.user_gateway import UserGateway
import getpass
from werkzeug.security import generate_password_hash


def create_superuser():
    print("Start create superuser to system")
    email = input("Input email: ")
    first_name = input("Input first name: ")
    last_name = input("Input last name: ")
    password = getpass.getpass("Input password: ")
    pw_hash = generate_password_hash(password)
    is_superuser = 1
    #print(email, first_name, last_name, pw_hash, is_superuser)
    user = UserGateway()
    user.create(email, first_name, last_name, pw_hash, is_superuser)
