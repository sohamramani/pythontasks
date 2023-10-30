from connection import *


# menu
def menu():
    print("\n1.Create Database \n"
        "2. Open Existing Database \n"
        "3. List All the Existing Database \n"
        "4. List All the Tables of specific Database \n"
        "5. Create New Table into Database \n"
        "6. Add New Column into Table\n"
        "7. Insert Records into Table \n"
        "8. Update Records of Table \n"
        "9. Delete Records from Table \n"
        "10. Display Data of Table\n"
        "11. Delete Existing column from Table \n"
        "12. Drop the Table \n")
    operation = input("please select an operation: ")
    print()
    return operation


#  1.Create Database
def create_database(cursor):
    try:
        dbname = input("pleaase enter database name you want to create: ")
        cursor.execute("CREATE DATABASE %s" %dbname)
    except Exception as e:
        print("ERROR: %s" %e)
        
# 2. Open Existing Database    
def use_database():
    databasename = input('Please select a database: ').strip()
    return databasename

# 3. List All the Existing Database
def database_list(cursor, query):
    cursor.execute(query)
    print("list of databases")
    for f in cursor:
        print(f)

# 4. List All the Tables of specific Database
def tables_list(cursor, query):
    try:
        cursor.execute(query)
        tables = cursor.fetchall()
        for x in tables:
            print(x)
    except Exception as e:
        print("ERROR: %s" %e)
    
# 5. Create New Table into Database   
def create_table(cursor):
    try:
        tablename = input("please enter table name: ")
        columnn1ame = input("please enter first column name: ")
        column1type = input("please enter first column type: ")
        columnn2ame = input("please enter second column name: ")
        column2type = input("please enter second column type: ")
        cursor.execute("CREATE TABLE {} ({} {}, {} {})".format(tablename, columnn1ame, column1type, columnn2ame, column2type))
        print("table created")
    except Exception as e:
        print("ERROR: %s" %e)

# 6. Add New Column into Table
def add_column(cursor):
    try:
        tablename = input("please enter table name: ")
        columnname = input("please enter column name: ")
        columntype = input("please enter column type: ")
        cursor.execute("ALTER TABLE {} ADD {} {}".format(tablename, columnname, columntype))
        print("column added")
    except Exception as e:
        print("ERROR: %s" %e)
        
# 7. Insert Records into Table
def insert_record(cursor):
    try:
        tablename = input("please enter table name: ")
        columnname = input("please enter column name: ")
        columnvalue = input("please enter the value for that column: ")
        cursor.execute("INSERT INTO {} ({}) VALUES ('{}')".format(tablename, columnname, columnvalue))
        print(cursor.execute)
        print("Record inserted successfully")
    except Exception as e:
        print("ERROR: %s" %e)
        
# 8. Update Records of Table
def update_record(cursor):
    try:
        tablename = input("please enter table name: ")
        setcolumnname = input("please enter column name in which you want to updare record: ")
        setcolumnvalue = input("please enter the new value for that column: ")
        wherecolumnname = input("please enter column name for where clause: ")
        wherecolumnvalue = input("please enter column value for where clause: ")
        cursor.execute("UPDATE {} SET {} = '{}' WHERE {} = '{}'".format(tablename, setcolumnname, setcolumnvalue, wherecolumnname, wherecolumnvalue))
        print("record updated successfully")
    except Exception as e:
        print("ERROR: %s" %e)
    
# 9. Delete Records from Table
def delete_record(cursor):
    try:
        tablename = input("please enter table name: ")
        columnname = input("please enter column name: ")
        columnvalue = input("please enter the value for that column: ")
        cursor.execute("DELETE FROM {} WHERE {}='{}'".format(tablename, columnname, columnvalue))
        print("record deleted")
    except Exception as e:
        print("ERROR: %s" %e) 
        
# 10. Display Data of Table
def display_table_data(cursor):
    try:
        tablename = input("please enter table name: ")
        cursor.execute("SELECT * FROM {}".format(tablename))
        rows = cursor.fetchall()
        
        for row in rows:
            for col in row:
                print(col,end=" ")
            print()            
    except Exception as e:
        print("ERROR: %s" %e) 

# 11. Delete Existing column from Table
def drop_column(cursor):
    try:
        tablename = input("please enter table name: ")
        columnname = input("please enter column name: ")
        cursor.execute("ALTER TABLE {} DROP COLUMN {}".format(tablename, columnname))
        print("column deleted")
    except Exception as e:
        print("ERROR: %s" %e) 

# 12. Drop the Table
def drop_table(cursor):
    try:
        tablename = input("please enter table name: ")
        cursor.execute("DROP TABLE {}".format(tablename))
        print("table deleted")
    except Exception as e:
        print("ERROR: %s" %e)
