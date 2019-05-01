import mysql.connector

config = {
  'user': 'surdo_user',
  'password': 'user_password',
  'host': '127.0.0.1',
  'database': 'surdoDB',
  'raise_on_warnings': True
}

surdoDB = mysql.connector.connect(**config)

cursor = surdoDB.cursor()

cursor.execute("select username from auth_user")

print(cursor)

for d in cursor:
    print(d)
data = cursor.fetchone()
print(data)

surdoDB.close()