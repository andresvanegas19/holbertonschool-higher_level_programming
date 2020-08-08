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

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            ORDER BY 1 LIMIT 15
            """)
        rows = cur.fetchall()

        for row in rows:
            print(row)

    # This is for close
    db.close()

