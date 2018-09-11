import pymysql

conn = None
try:
    # 建立连接
    conn = pymysql.connect('192.168.86.100', 'root', 'root', 'test')
    print(conn.ping(False))
    # 获取游标cursor
    cursor = conn.cursor()
    sql = 'insert into reg values (4, 'jr', 'jr', 'jr')
    cursor.execute(sql)


    conn.commit()
except:
    conn.rollback()
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()













