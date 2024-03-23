#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3], port=3306)
    chaima = database.cursor()
    chaima.execute("SELECT * FROM states")
    rows = chaima.fetchall()
    for row in rows:
        print(row)
    chaima.close()
    database.close()
