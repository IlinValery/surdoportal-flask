from application.gateway.connection import *
from application.base_classes import LogBase


class LogGateway(LogBase):
    connection = DatabaseConnection()

    def create(self):
        cursor = self.connection.db.cursor()
        request = "INSERT INTO log (`user`, `table`, `element`, `action`) VALUES (%s, %s, %s, %s);"
        data = (self.user, self.table, self.element, self.action)

        try:
            cursor.execute(request, data)
            self.connection.db.commit()
            return {"code": 0, "message": "Log was added successfully"}
        except IntegrityError:
            return {"code": 1, "message": "Error to add log!"}

    def read_last(self, count=100):
        cursor = self.connection.db.cursor()
        result = None
        #request = "SELECT * FROM log"
        request = "SELECT * FROM log ORDER BY date_time DESC LIMIT %s"
        data = (count,)
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

    def read_by_user_id(self, user_id, count=10):
        cursor = self.connection.db.cursor()
        result = None
        request = "SELECT * FROM log  WHERE user = %s ORDER BY date_time DESC LIMIT %s"
        data = (user_id, count)
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
