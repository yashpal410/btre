'''
import random





tup = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k',
       'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
       'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

str1 = ''

def alphanum(tup):
    for i in range(7):
        p=random.choice(tup)
        str1=str1+p
    return str1
'''
import random
import sqlite3
from sqlite3 import Error

tup = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D',
'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')



def alphanum(tup):
	str1 = ''
	for i in range(7):
		p=random.choice(tup)
		str1 = str1 + p
	return str1

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

#   """ create a database connection to the SQLite database
#       specified by db_file
#    :param db_file: database file
#    :return: Connection object or None
#    """
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
#        #c.execute("drop table projects;")
    except Error as e:
        print(e)
#     """ create a table from the create_table_sql statement
#     :param conn: Connection object
#     :param create_table_sql: a CREATE TABLE statement
#     :return:
#     """
def insertion(conn):
    x = alphanum(tup)
    query = "INSERT INTO projects VALUES ('{}')".format(x)
    query2 = "SELECT * FROM projects"
    try:
        c = conn.cursor()
#              #c.execute("INSERT INTO projects VALUES ('ROHAN')")
        c.execute(query)
        c.execute(query2)
        rows = c.fetchall()
        for row in rows:
            print(row[0])
        print(x)
        conn.commit()
    except:
        insertion(conn)

def main():
    database = r"E:\sqlite\db\pythonsqlite.db"
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                            name text  UNIQUE
                                        ); """
    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_projects_table)
        insertion(conn)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
