import pymysql

    
def mysql_database(dbname = None):
    db = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "soham2063",
        database = dbname
    )
    cursor = db.cursor()
    db.autocommit = True
    return cursor
mysql_database()