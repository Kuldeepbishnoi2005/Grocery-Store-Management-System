from sql_connection import get_sql_connection

cnx = get_sql_connection()
cursor = cnx.cursor()
cursor.execute("SHOW TABLES;")

for table in cursor:
    print(table)
