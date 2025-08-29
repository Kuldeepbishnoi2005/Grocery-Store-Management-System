import datetime
import mysql.connector

__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
      __cnx = mysql.connector.connect(host='localhost', port=3306,user='root', password='@Bishnoi29', database='grocerystore')

  return __cnx

