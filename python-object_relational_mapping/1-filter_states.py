#!/usr/bin/python3
""" Program lists all states with a name
starting with N from the database"""


import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
       user=sys.argv[1],
       password=sys.argv[2],
       db=sys.argv[3],
       host="localhost",
       port=3306
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states \
        WHERE name LIKE BINARY 'N%' \
        ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()
