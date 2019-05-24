from application.gateway.connection import *
from application.visitor.visitor_component import VisitorComponent
from application.visitor.visitor import Visitor


class TeacherGateway(VisitorComponent):
    connection = DatabaseConnection()

    def create(self, name, department_id):
        cursor = self.connection.db.cursor()
        request = "INSERT INTO teacher (name, department_id) VALUES (%s, %s)"
        data = (name, department_id)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            cursor.close()
            return {"code": 0, "message": "Department was created successfully"}
        except IntegrityError:
            cursor.close()
            return {"code": 1, "message": "Error to create department"}

    def read_all(self):
        cursor = self.connection.db.cursor()
        result = None
        request = "SELECT * FROM teacher"
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

    def read_by_id(self, teacher_id):
        cursor = self.connection.db.cursor()
        result = None
        request = "SELECT * FROM teacher WHERE idteacher = %s"
        data = (teacher_id,)
        cursor.execute(request, data)
        cursor_output = cursor.fetchone()
        if cursor_output:
            fields = map(lambda x: x[0], cursor.description)
            result = dict(zip(fields, cursor_output))
        cursor.close()
        return result

    def update(self, name, department_id, teacher_id):
        cursor = self.connection.db.cursor()
        result = None
        request = "UPDATE teacher SET name = %s, department_id = %s WHERE (idteacher = %s)"
        data = (name, department_id, teacher_id)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            cursor.close()
            return {"code": 0, "message": "Department was changed successfully"}
        except IntegrityError:
            cursor.close()
            return {"code": 1, "message": "Error to change department"}

    def delete(self, teacher_id):
        cursor = self.connection.db.cursor()
        result = None
        request = "DELETE FROM teacher WHERE (idteacher = %s)"
        data = (teacher_id,)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            cursor.close()
            return {"code": 0, "message": "Department was deleted successfully"}
        except IntegrityError:
            cursor.close()
            return {"code": 1, "message": "Something went wrong"}


    def access_get_number(self, visitor: Visitor):
        return visitor.get_teacher_number(self, element=self)