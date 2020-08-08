#!/usr/bin/python3
"""This script execute in env of sqlldb
    (no argument validation needed)"""

import MySQLdb
import sys


if __name__ == "__main__":
    # script should take 3 arguments: mysql username, mysql
    # password and database name
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cur = db.cursor()
    query = """SELECT * FROM """ + sys.argv[3] + \
        """.states WHERE name LIKE 'N%' ORDER BY id"""
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    # This is for close
    db.close()
    cur.close()
