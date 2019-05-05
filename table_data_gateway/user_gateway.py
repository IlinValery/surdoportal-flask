from application.settings import mysql


class UserGateway(object):

    def create(self, email, first_name, second_name, password, is_superuser):
        cursor = mysql.connection.cursor()
        request = "INSERT INTO users (email, first_name, second_name, password, is_superuser)" \
                  "VALUES ('{email_field}', '{first_name_field}', '{second_name_field}', '{password_field}'," \
                  "'{is_superuser_field}'".format(email_field=email, first_name_field=first_name,
                                                  second_name_field=second_name, password_field=password,
                                                  is_superuser_field = is_superuser)
        print("request is:", request)
