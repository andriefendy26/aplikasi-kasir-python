import mysql.connector

class konekDB:
    def __init__(self):
        pass

    def querryResult(self, strsql):
        cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='warung')
        conn = cnx.cursor()
        conn.execute(strsql)
        result = conn.fetchall()
        return result
        pass


    def querryExecute(self, strsql):
        cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='warung')
        conn = cnx.cursor()
        conn.execute(strsql)
        cnx.commit()
        pass
