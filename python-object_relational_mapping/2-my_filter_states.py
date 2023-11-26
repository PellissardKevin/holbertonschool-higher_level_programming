#!/usr/bin/python3
"""Module listing all Arizona name from the database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cur = db.cursor()
    cur.execute(
        """SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"""
        .format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()
