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
        print("cur_output", cursor_output)
        return cursor_output[0]

    def get_discipline_number(self, element):
        cursor = element.connection.db.cursor()
        request = "SELECT MAX(iddiscipline) FROM discipline"
        cursor.execute(request)
        cursor_output = cursor.fetchone()
        print("cur_output", cursor_output)
        return cursor_output[0]

    def get_teacher_number(self, element):
        cursor = element.connection.db.cursor()
        request = "SELECT MAX(idteacher) FROM teacher"
        cursor.execute(request)
        cursor_output = cursor.fetchone()
        print("cur_output", cursor_output)
        return cursor_output[0]
