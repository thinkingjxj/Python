import cx_oracle

conn = cx_oracle.connect("")
cursor = conn.cursor()

lst = [0.6, 0.7, 0, 8, 0.85, 0.9, 0.95, 0.96, 0.97, 0.08, 0.99]


def create_table():
    conn.execute("CREATE TABLE model_predict ("
                 "ID NUMBER(8) PRIMARY KEY, S VARCHAR2(16), TP VARCHAR2(16), FP VARCHAR2(16), "
                 "TN VARCHAR2(16), FN VARCHAR2(16),  r VARCHAR2(16), p VARCHAR2(16), F VARCHAR2(16), A VARCHAR2(16))")
    conn.commit()


def insert_data(score):
    sql = "insert into model_predict '', '', " \
              "(select count(*) from gl_qiedian a where a.label==1 and a.score>=" + score +")," \
              "(select count(*) from gl_qiedian a where a.label==0 and a.score>=" + score +"), " \
              "(select count(*) from gl_qiedian a where a.label==1 and a.score<" + score +"), " \
              "(select count(*) from gl_qiedian a where a.label==0 and a.score<" + score +"),  '','','','' from dual"
    cursor.execute(sql)
    conn.commit()
    cursor.execute("UPDATE model_predict SET "
                   "r=TRUNC(TP/(TP + FN), 4), "
                   "P=TRUNC(TP/(TP+FP),4),"
                   "F=TRUNC(2*P*R/(P+R),4),"
                   "A=TRUNC((TN+TP)/(select count(*)  from gl_qiedian),4)")
    conn.commit()



