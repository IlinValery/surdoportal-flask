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



# app.config["MYSQL_USER"] = "surdo_user"
# app.config["MYSQL_PASSWORD"] = "UserPass123)"
# app.config["MYSQL_DB"] = "surdoDB"
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"
# app.config["JWT_SECRET_KEY"] = "jmTVPowuEd4YPRbPMDySmfhXYuczUb4F"