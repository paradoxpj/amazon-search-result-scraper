import mysql.connector

from dotenv import load_dotenv
import os


def setup_db(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE items (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
    mycursor.execute("CREATE TABLE prices (price INT NOT NULL, itemid INT, record_date DATE, FOREIGN KEY (itemid) REFERENCES items(id))")

def manage_db():
    load_dotenv()
    mydb = mysql.connector.connect(
      host = os.environ.get("mysql_host"),
      user = os.environ.get("mysql_user"),
      password = os.environ.get("mysql_password"),
      database = os.environ.get("mysql_database"),
    )
    setup_db(mydb)

if __name__ == '__main__':
    '''main function'''
    manage_db()
