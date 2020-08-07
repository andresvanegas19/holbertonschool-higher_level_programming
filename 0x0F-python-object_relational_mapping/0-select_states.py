#!/usr/bin/python3
"""This script execute in env of sqlldb
    (no argument validation needed)"""

import MySQLdb
import sys


if __name__ == "__main__":
    # script should take 3 arguments: mysql username, mysql password and database name

    MySQLdb.connect(host=MY_HOST, port=3306, user=sys.argv[1], passwd=1, db="hbtn_0e_0_usa")


