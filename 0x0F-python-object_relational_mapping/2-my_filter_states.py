#!/usr/bin/python3
""" takes in an argument and displays all values in the states table """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(argv[4]))
    result = cur.fetchall()
    for i in result:
        print(i)
    cur.close()
    db.close()
