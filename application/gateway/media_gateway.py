from application.gateway.connection import *
from application.visitor.visitor_component import VisitorComponent
from application.visitor.visitor import Visitor


class MediaGateway(VisitorComponent):
    connection = DatabaseConnection()
    types = {"sign": 1, "articulation": 2, "example": 3}

    def create(self, type, youtube_id, term_id):
        cursor = self.connection.db.cursor()
        request = "INSERT INTO media (type, youtube_id, term) VALUES (%s, %s, %s)"
        data = (self.types[type], youtube_id, term_id)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            cursor.close()
            return {"code": 0, "message": "Media was created successfully"}
        except IntegrityError:
            cursor.close()
            return {"code": 1, "message": "Error to create media"}

    def read_all(self):
        cursor = self.connection.db.cursor()
        result = None
        request = "SELECT * FROM media"
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


    def read_by_term(self, term_id):
        cursor = self.connection.db.cursor()
        result = None
        request = "SELECT * FROM media WHERE term = %s order by type"
        data = (term_id,)
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

    def update(self, media_id, type, youtube_id,):
        cursor = self.connection.db.cursor()
        result = None
        request = "UPDATE media SET type = %s, youtube_id = %s WHERE (idmedia = %s)"
        data = (self.types[type], youtube_id, media_id)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            cursor.close()
            return {"code": 0, "message": "Media was changed successfully"}
        except IntegrityError:
            cursor.close()
            return {"code": 1, "message": "Error to change media"}

    def delete(self, media_id):
        cursor = self.connection.db.cursor()
        result = None
        request = "DELETE FROM media WHERE (idmedia = %s)"
        data = (media_id,)
        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            cursor.close()
            return {"code": 0, "message": "Media was deleted successfully"}
        except IntegrityError:
            cursor.close()
            return {"code": 1, "message": "Something went wrong"}


    def access_get_number(self, visitor: Visitor):
        return visitor.get_media_number(self, element=self)