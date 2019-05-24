from application.gateway.connection import *
from application.visitor.visitor_component import VisitorComponent
from application.visitor.visitor import Visitor

class UserGateway(VisitorComponent):
    connection = DatabaseConnection()

    def create(self, email, first_name, last_name, pw_hash, is_superuser):
        cursor = self.connection.db.cursor()
        request = "INSERT INTO user (email, first_name, last_name, password, is_superuser) VALUES" \
                  "(%s, %s, %s, %s, %s)"
        data = (email, first_name, last_name, pw_hash, is_superuser)

        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            cursor.close()
            return {"code": 0, "message": "User was created successfully"}
        except IntegrityError:
            cursor.close()
            return {"code": 1, "message": "Error to load user with same name"}

    def read_all(self):
        cursor = self.connection.db.cursor()
        result = None
        request = "SELECT iduser, email, first_name, last_name, is_superuser FROM user"
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
        cursor.close()
        return result

    def read_by_id(self, user_id):
        cursor = self.connection.db.cursor()
        result = None
        request = "SELECT iduser, email, first_name, last_name, is_superuser FROM user WHERE iduser = %s"
        data = (user_id,)

        cursor.execute(request, data)
        cursor_output = cursor.fetchone()
        if cursor_output:
            fields = map(lambda x: x[0], cursor.description)
            result = dict(zip(fields, cursor_output))
        cursor.close()
        return result

    def read_by_email(self, user_email):
        cursor = self.connection.db.cursor()
        result = None
        request = "SELECT * FROM user WHERE email=%s"
        data = (user_email,)
        cursor.execute(request, data)
        cursor_output = cursor.fetchone()
        if cursor_output:
            fields = map(lambda x: x[0], cursor.description)
            result = dict(zip(fields, cursor_output))
        cursor.close()
        return result

    def update_fields(self, id_user, email, first_name, last_name, is_superuser):
        cursor = self.connection.db.cursor()
        result = None
        request = "UPDATE user SET email = %s, first_name = %s, last_name = %s, is_superuser = %s WHERE (iduser = %s)"
        data = (email, first_name, last_name, is_superuser, id_user)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            cursor.close()
            return {"code": 0, "message": "User was changed successfully"}
        except IntegrityError:
            cursor.close()
            return {"code": 1, "message": "Error to load user with same name"}

    def update_password(self, id_user, pw_hash):
        cursor = self.connection.db.cursor()
        result = None
        request = "UPDATE user SET password = %s  WHERE (iduser = %s)"
        data = (pw_hash, id_user)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            cursor.close()
            return {"code": 0, "message": "User password was changed successfully"}
        except IntegrityError:
            cursor.close()
            return {"code": 1, "message": "Something went wrong"}

    def delete(self, user_id):
        cursor = self.connection.db.cursor()
        result = None
        request = "DELETE FROM user WHERE (iduser = %s)"
        data = (user_id,)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            cursor.close()
            return {"code": 0, "message": "User was deleted successfully"}
        except IntegrityError:
            cursor.close()
            return {"code": 1, "message": "Something went wrong"}

    def access_get_number(self, visitor: Visitor):
        return visitor.get_user_number(self, element=self)
