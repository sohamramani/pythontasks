from operation import *
from connection import *


while True:
    operation = menu()
    if operation == "1":
        create_database(psql_database())
    elif operation == '2':
        database = use_database()
        psql_database(database)
    elif operation == '3':
        database_list(psql_database(), "SELECT datname FROM pg_database WHERE datistemplate = false;")
    elif operation == '4':
        db = input("pleaase enter database name: ")
        tables_list(psql_database(db), "SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';")
    elif operation == '5':
        db = input("pleaase enter database name: ")
        create_table(psql_database(db))
    elif operation == '6':
        db = input("pleaase enter database name in which table is exist: ")
        add_column(psql_database (db))
    elif operation == '7':
        db = input("pleaase enter database name in which table is exist: ")
        insert_record(psql_database (db))
    elif operation == '8':
        db = input("pleaase enter database name in which table is exist: ")
        update_record(psql_database(db))
    elif operation == '9':
        db = input("pleaase enter database name in which table is exist: ")
        delete_record(psql_database(db))
    elif operation == '10':
        db = input("pleaase enter database name in which table is exist: ")
        display_table_data(psql_database(db))
    elif operation == '11':
        db = input("pleaase enter database name in which table is exist: ")
        drop_column(psql_database(db))
    elif operation == '12':
        db = input("pleaase enter database name in which table is exist: ")
        drop_table(psql_database(db))