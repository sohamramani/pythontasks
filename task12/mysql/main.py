from operation import *
from connection import *


while True:
    operation = menu()
    if operation == "1":
        create_database(mysql_database())
    elif operation == '2':
        database = use_database()
        mysql_database(database)
    elif operation == '3':
        database_list(mysql_database(), "SHOW DATABASES")
    elif operation == '4':
        db = input("please enter database name: ")
        tables_list(mysql_database(db), "SHOW TABLES")
    elif operation == '5':
        db = input("please enter database name: ")
        create_table(mysql_database(db))
    elif operation == '6':
        db = input("please enter database name in which table is exist: ")
        add_column(mysql_database(db))
    elif operation == '7':
        db = input("please enter database name in which table is exist: ")
        insert_record(mysql_database(db))
    elif operation == '8':
        db = input("please enter database name in which table is exist: ")
        update_record(mysql_database(db))
    elif operation == '9':
        db = input("please enter database name in which table is exist: ")
        delete_record(mysql_database(db))
    elif operation == '10':
        db = input("please enter database name in which table is exist: ")
        display_table_data(mysql_database(db))
    elif operation == '11':
        db = input("please enter database name in which table is exist: ")
        drop_column(mysql_database(db))
    elif operation == '12':
        db = input("please enter database name in which table is exist: ")
        drop_table(mysql_database(db))