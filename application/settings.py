from flask import Flask, jsonify, request, json
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager



app = Flask(__name__)


cors = CORS(app)
mysql = MySQL(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

app.config["MYSQL_USER"] = "surdo_user"
app.config["MYSQL_PASSWORD"] = "UserPass123)"
app.config["MYSQL_DB"] = "surdoDB"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config["JWT_SECRET_KEY"] = "jmTVPowuEd4YPRbPMDySmfhXYuczUb4F"