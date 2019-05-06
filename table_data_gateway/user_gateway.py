from application.settings import mysql, bcrypt
from application.connection import *


class UserGateway(object):
    def __init__(self, user_id=None, user_email=str(), user_fn="", user_sn="", user_pass="secret_pass", user_su=0):
        self.id = user_id
        self.email = user_email
        self.first_name = user_fn
        self.second_name = user_sn
        self.password = bcrypt.generate_password_hash(user_pass).decode('utf')
        self.is_superuser = user_su
        self.connection = DatabaseConnection()

    def create(self):
        cursor = self.connection.db.cursor()
        request = "INSERT INTO user (email, first_name, second_name, password, is_superuser) VALUES" \
                  "(%s, %s, %s, %s, %s)"
        data = (self.email, self.first_name, self.second_name, self.password, self.is_superuser)

        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            return 0
        except IntegrityError:
            return {"err": "Error to load user with same name"}

    def read(self, by_email=False, by_all=False, count=0):
        cursor = self.connection.db.cursor()
        request = ""
        data = ()
        result = None
        if by_all:
            request = "SELECT iduser, email, first_name, second_name, is_superuser FROM user"

            #TODO prepare for pagination

            cursor.execute(request)
            cursor_output = cursor.fetchall()
            if cursor_output:
                fields = cursor.description
                result = []
                for row in cursor_output:
                    tmp = {}
                    for (index, column) in enumerate(row):
                        tmp[fields[index][0]] = column
                    result.append(tmp)

        else:
            if by_email:
                request = "SELECT * FROM user WHERE email=%s"
                data = (self.email,)
            else:
                request = "SELECT iduser, email, first_name, second_name, is_superuser FROM user WHERE iduser = %s"
                data = (self.id,)

            cursor.execute(request, data)
            cursor_output = cursor.fetchone()
            if cursor_output:
                fields = map(lambda x: x[0], cursor.description)
                result = dict(zip(fields, cursor_output))
            print(result)
        return result

    def update(self):
        pass

    def delete(self):
        pass