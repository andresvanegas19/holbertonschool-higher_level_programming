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

    # cursor.execute("SELECT admin FROM users
    # WHERE username = %s'", (username, ));
    # cursor.execute("SELECT admin FROM users WHERE username =
    # %(username)s", {'username': username});

    with db.cursor() as cur:
        fill = {'name': sys.argv[4]}
        cur.execute("""
            SELECT * FROM
                states
            WHERE
                name = %(name)s
            ORDER BY
                id""", fill)
        rows = cur.fetchall()

        for row in rows:
            print(row)

    # This is for close
    db.close()
