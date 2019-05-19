import MySQLdb
from MySQLdb import IntegrityError


class DatabaseConnection:
    def __init__(self):
        self.db = MySQLdb.connect(
            host="localhost",
            user="surdo_user",
            passwd="UserPass123)",
            db="surdoDB",
            charset="utf8",

        )
