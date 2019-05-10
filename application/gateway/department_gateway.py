from application.gateway.connection import *
from application.base_classes import DepartmentBase


class DepartmentGateway(DepartmentBase):
    connection = DatabaseConnection()

    def create(self):
        cursor = self.connection.db.cursor()
        request = "INSERT INTO department (caption, initials) VALUES (%s, %s)"
        data = (self.caption, self.initials)

        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            return {"code": 0, "message": "Department was created successfully"}
        except IntegrityError:
            return {"code": 1, "message": "Error to create department"}

    def read_all(self):
        cursor = self.connection.db.cursor()
        result = None
        request = "SELECT * FROM department"
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

    def read_by_id(self, department_id):
        cursor = self.connection.db.cursor()
        result = None
        request = "SELECT * FROM department WHERE iddepartment = %s"
        data = (department_id,)

        cursor.execute(request, data)
        cursor_output = cursor.fetchone()
        if cursor_output:
            fields = map(lambda x: x[0], cursor.description)
            result = dict(zip(fields, cursor_output))
        return result

    def update(self):
        cursor = self.connection.db.cursor()
        result = None
        request = "UPDATE department SET caption = %s, initials = %s WHERE (iddepartment = %s)"
        data = (self.caption, self.initials, self.id)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            return {"code": 0, "message": "Department was changed successfully"}
        except IntegrityError:
            return {"code": 1, "message": "Error to change department"}

    def delete(self):
        cursor = self.connection.db.cursor()
        result = None
        request = "DELETE FROM department WHERE (iddepartment = %s)"
        data = (self.id,)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            return {"code": 0, "message": "Department was deleted successfully"}
        except IntegrityError:
            return {"code": 1, "message": "Something went wrong"}
