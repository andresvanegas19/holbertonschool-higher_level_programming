#!/usr/bin/python3
"""This script execute in env of sqlldb
     (no argument validation needed)"""

import MySQLdb
import sys


if __name__ == "__main__" and len(sys.argv) == 5:

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
                DISTINCT cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name = %(name_state)s
            """, {'name_state': sys.argv[4]})
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append(row[0])
        print(', '.join(result), sep='')
    # This is for close
    db.close()
