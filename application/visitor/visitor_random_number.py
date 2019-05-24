from application.visitor.visitor import Visitor


class VisitorRandomNumber(Visitor):

    def get_user_number(self, element):
        pass

    def get_department_number(self, element):
        pass

    def get_discipline_number(self, element):
        pass

    def get_teacher_number(self, element):
        pass

    def get_term_number(self, element):
        cursor = element.connection.db.cursor()
        request = "SELECT idterm FROM term WHERE is_shown = 1 ORDER BY RAND() LIMIT 1"
        cursor.execute(request)
        cursor_output = cursor.fetchone()
        cursor.close()
        return cursor_output[0]

    def get_media_number(self, element):
        pass
