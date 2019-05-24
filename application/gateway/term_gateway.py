from application.gateway.connection import *
from application.visitor.visitor_component import VisitorComponent
from application.visitor.visitor import Visitor


class TermGateway(VisitorComponent):
    connection = DatabaseConnection()

    def create(self, caption, description, discipline, teacher, lesson, image_path, creator, is_shown = 0):
        cursor = self.connection.db.cursor()
        request = "INSERT INTO term (caption, description, lesson, teacher, discipline, image_path, creator, is_shown) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (caption, description, lesson, teacher, discipline, image_path, creator, is_shown)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            cursor.close()
            return {"code": 0, "message": "Term was created successfully"}
        except IntegrityError:
            cursor.close()
            return {"code": 1, "message": "Error to create term"}

    def read_for_editor(self, start=0, end=100, only_invalided=False, discipline_id=0, user_id=0):
        cursor = self.connection.db.cursor()
        result = None
        request = ""
        data = ()
        data_limit = (start,end)
        if (only_invalided or discipline_id or user_id):
            request = "SELECT * FROM term WHERE "
            has_parameter = False
            if only_invalided:
                has_parameter = True
                request += "is_shown = %s"
                data += (0,)
            if discipline_id!=0:
                if has_parameter:
                    request+=' AND '
                has_parameter = True
                request += "discipline = %s"
                data += (discipline_id,)
            if user_id!=0:
                if has_parameter:
                    request+=' AND '
                request += "creator = %s"
                data += (user_id,)
            data += data_limit
            request+= " order by is_shown ASC, changed DESC LIMIT %s,%s"
        else:
            request = "SELECT * FROM term order by is_shown ASC, changed DESC LIMIT %s,%s"
            data = data_limit
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
        cursor.close()
        return result

    def read_for_view(self, start=0, end=100, discipline_id=0, phrase=""):
        cursor = self.connection.db.cursor()
        result = None
        request = ""
        data = ()
        data_limit = (start,end)
        if (discipline_id or phrase!=""):
            request = "SELECT * FROM term WHERE is_shown = 1 AND "
            has_parameter = False
            if discipline_id!=0:
                has_parameter = True
                request += "discipline = %s"
                data += (discipline_id,)
            if phrase!="":
                if has_parameter:
                    request+=' AND '
                request += "LOWER(caption) LIKE LOWER(%s)"
                phrase_formated = "%"+phrase+"%"
                data += (phrase_formated,)
            data += data_limit
            request+= " ORDER BY lesson LIMIT %s,%s"
        else:
            request = "SELECT * FROM term WHERE is_shown = 1 ORDER BY lesson LIMIT %s,%s"
            data = data_limit
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
        cursor.close()
        return result

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
        cursor.close()
        return result

    def update(self, term_id,  caption, description, discipline, teacher, lesson, image_path, is_shown):
        cursor = self.connection.db.cursor()
        result = None
        request = "UPDATE term SET caption = %s, description = %s, lesson= %s, teacher= %s, discipline= %s, image_path= %s, is_shown= %s WHERE (idterm = %s)"
        data = (caption, description, lesson, teacher, discipline, image_path, is_shown, term_id)

        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            cursor.close()
            return {"code": 0, "message": "Term was changed successfully"}
        except IntegrityError:
            cursor.close()
            return {"code": 1, "message": "Error to change term"}

    def update_validation(self, term_id, is_shown):
        cursor = self.connection.db.cursor()
        result = None
        request = "UPDATE term SET is_shown= %s WHERE (idterm = %s)"
        data = (is_shown, term_id)

        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            cursor.close()
            return {"code": 0, "message": "Term validation was changed successfully"}
        except IntegrityError:
            cursor.close()
            return {"code": 1, "message": "Error to change term validation"}
        pass

    def delete(self, term_id):
        cursor = self.connection.db.cursor()
        result = None
        request = "DELETE FROM term WHERE (idterm = %s)"
        data = (term_id,)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            cursor.close()
            return {"code": 0, "message": "Term was deleted successfully"}
        except IntegrityError:
            cursor.close()
            return {"code": 1, "message": "Something went wrong"}


    def access_get_number(self, visitor: Visitor):
        return visitor.get_term_number(self, element=self)