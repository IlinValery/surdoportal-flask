from application.visitor.visitor import Visitor


class VisitorLastNumber(Visitor):

    def get_user_number(self, element):
        cursor = element.connection.db.cursor()
        request = "SELECT MAX(iduser) FROM user"
        cursor.execute(request)
        cursor_output = cursor.fetchone()
        return cursor_output[0]

    def get_department_number(self, element):
        cursor = element.connection.db.cursor()
        request = "SELECT MAX(iddepartment) FROM department"
        cursor.execute(request)
        cursor_output = cursor.fetchone()
        return cursor_output[0]
