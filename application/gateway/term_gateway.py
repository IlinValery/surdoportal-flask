from application.gateway.connection import *
from application.base_classes import TermBase
from application.visitor.visitor_component import VisitorComponent
from application.visitor.visitor import Visitor


class TermGateway(TermBase, VisitorComponent):
    connection = DatabaseConnection()

    def create(self):
        cursor = self.connection.db.cursor()
        request = "INSERT INTO term (caption, description, lesson, teacher, discipline, image_path, creator, is_shown) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (self.caption, self.description, self.lesson, self.teacher, self.discipline, self.image_path, self.creator, self.is_shown)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            return {"code": 0, "message": "Term was created successfully"}
        except IntegrityError:
            return {"code": 1, "message": "Error to create term"}

    def read_all(self, start=0, end=100, for_public=True, only_invalided=True):
        cursor = self.connection.db.cursor()
        result = None
        request = "SELECT * FROM term LIMIT %s,%s"
        data = (start, end)
        cursor.execute(request, data)
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

    def read_by_discipline(self, discipline_id):
        #TODO Read by discipline (many terms)
        pass

    def read_by_creator(self, user_id):
        #TODO Read by creator (many terms)
        pass


    def read_by_id(self, term_id):
        cursor = self.connection.db.cursor()
        result = None
        request = "SELECT * FROM term WHERE idterm = %s"
        data = (term_id,)
        cursor.execute(request, data)
        cursor_output = cursor.fetchone()
        if cursor_output:
            fields = map(lambda x: x[0], cursor.description)
            result = dict(zip(fields, cursor_output))
        return result

    def update(self):
        #TODO Update term with all params
        cursor = self.connection.db.cursor()
        result = None
        request = "UPDATE term SET name = %s, department_id = %s WHERE (idteacher = %s)"
        data = (self.name, self.department, self.id)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            return {"code": 0, "message": "Department was changed successfully"}
        except IntegrityError:
            return {"code": 1, "message": "Error to change department"}

    def update_validation(self):
        #TODO (its empty validation for term)
        pass

    def delete(self):
        cursor = self.connection.db.cursor()
        result = None
        request = "DELETE FROM term WHERE (idterm = %s)"
        data = (self.id,)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            return {"code": 0, "message": "Term was deleted successfully"}
        except IntegrityError:
            return {"code": 1, "message": "Something went wrong"}


    def access_get_number(self, visitor: Visitor):
        return visitor.get_term_number(self, element=self)