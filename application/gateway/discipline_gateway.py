from application.gateway.connection import *
from application.base_classes import DisciplineBase
from application.visitor.visitor_component import VisitorComponent
from application.visitor.visitor import Visitor


class DisciplineGateway(DisciplineBase, VisitorComponent):
    connection = DatabaseConnection()

    def create(self):
        cursor = self.connection.db.cursor()
        request = "INSERT INTO discipline (name, semester, department_id) VALUES (%s, %s, %s)"
        data = (self.name, self.semester, self.department)

        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            return {"code": 0, "message": "Department was created successfully"}
        except IntegrityError:
            return {"code": 1, "message": "Error to create department"}

    def read_all(self):
        cursor = self.connection.db.cursor()
        result = None
        request = "SELECT * FROM discipline"
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

    def read_by_id(self, discipline_id):
        cursor = self.connection.db.cursor()
        result = None
        request = "SELECT * FROM discipline WHERE iddiscipline = %s"
        data = (discipline_id,)

        cursor.execute(request, data)
        cursor_output = cursor.fetchone()
        if cursor_output:
            fields = map(lambda x: x[0], cursor.description)
            result = dict(zip(fields, cursor_output))
        return result

    def read_by_department(self, department_id):
        pass

    def update(self):
        cursor = self.connection.db.cursor()
        result = None
        request = "UPDATE discipline SET name = %s, semester = %s, department_id = %s WHERE (iddiscipline = %s)"
        data = (self.name, self.semester, self.department, self.id)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            return {"code": 0, "message": "Department was changed successfully"}
        except IntegrityError:
            return {"code": 1, "message": "Error to change department"}

    def delete(self):
        cursor = self.connection.db.cursor()
        result = None
        request = "DELETE FROM discipline WHERE (iddiscipline = %s)"
        data = (self.id,)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            return {"code": 0, "message": "Department was deleted successfully"}
        except IntegrityError:
            return {"code": 1, "message": "Something went wrong"}


    def access_get_number(self, visitor: Visitor):
        return visitor.get_discipline_number(self, element=self)