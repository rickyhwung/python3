import pymysql

config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "root",
    "database": "test"
}

db = pymysql.connect(**config)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
sql = "SELECT * FROM file_control"
cursor.execute(sql)
res = cursor.fetchall()
print(res)
cursor.close()
db.close()
