#!/usr/bin/python3
"""Script that takes in an argument and
displays all values in the states"""


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
    sql = """ SELECT * FROM states
        WHERE name LIKE BINARY '{}'
        ORDER BY id ASC """.format(sys.argv[4])

    cursor.execute(sql)
    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    conn.close()
