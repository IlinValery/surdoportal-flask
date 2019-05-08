from application.connection import *
from table_data_gateway.base_classes import UserBase


class UserGateway(UserBase):
    connection = DatabaseConnection()

    def create(self):
        cursor = self.connection.db.cursor()
        request = "INSERT INTO user (email, first_name, last_name, password, is_superuser) VALUES" \
                  "(%s, %s, %s, %s, %s)"
        data = (self.email, self.first_name, self.last_name, self.password, self.is_superuser)

        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            return {"code": 0, "message": "User was changed successfully"}
        except IntegrityError:
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
        return result

    def update_fields(self):
        cursor = self.connection.db.cursor()
        result = None
        request = "UPDATE user SET email = %s, first_name = %s, last_name = %s, is_superuser = %s WHERE (iduser = %s)"
        data = (self.email, self.first_name, self.last_name, self.is_superuser, self.id)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            return {"code": 0, "message": "User was changed successfully"}
        except IntegrityError:
            return {"code": 1, "message": "Error to load user with same name"}

    def update_password(self):
        cursor = self.connection.db.cursor()
        result = None
        request = "UPDATE user SET password = %s  WHERE (iduser = %s)"
        data = (self.password, self.id)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            return {"code": 0, "message": "User password was changed successfully"}
        except IntegrityError:
            return {"code": 1, "message": "Something went wrong"}

    def delete(self):
        cursor = self.connection.db.cursor()
        result = None
        request = "DELETE FROM user WHERE (iduser = %s)"
        data = (self.id,)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            return {"success": "User was deleted successfully"}
        except IntegrityError:
            return {"error": "Something went wrong"}
        #DELETE FROM `surdoDB`.`user` WHERE (`iduser` = '1');
