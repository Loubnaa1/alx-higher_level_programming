#!/usr/bin/python3
"""  lists all states in hbtn_0e_0_usa """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (argv[4], ))
    result = cur.fetchall()
    for i in result:
        print(i)
    cur.close()
    db.close()
