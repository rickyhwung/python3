import pymysql

def connection(database_key):
    mysql = {'host': '', 'port': '', 'user': '', 'password': '', 'database': '', 'charset': 'utf8'}
    if database_key == 'hyfdb':
        mysql['host'] = '192.168.6.222'
        mysql['port'] = 3306
        mysql['user'] = 'hyf'
        mysql['password'] = 'hyf'
        mysql['database'] = 'hyfdb'
        mysql['cursorclass'] = pymysql.cursors.DictCursor
    elif database_key == 'test':
        mysql['host'] = '127.0.0.1'
        mysql['port'] = 3306
        mysql['user'] = 'root'
        mysql['password'] = ''
        mysql['database'] = 'test'
        mysql['cursorclass'] = pymysql.cursors.DictCursor
    return mysql

conn = pymysql.connect(**connection('test'))
cursor = conn.cursor()
