import psycopg2


def psql_database(dbname = 'postgres'):
    db = psycopg2.connect(
        database = dbname,
        user = "soham", 
        password = "2063", 
        host = "127.0.0.1", 
        port = "5432"
    )
    cursor = db.cursor()
    db.autocommit = True
    return cursor
