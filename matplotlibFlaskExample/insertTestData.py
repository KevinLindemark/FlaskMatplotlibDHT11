import sqlite3 as lite
import sys
con = lite.connect('database.db')
with con:
    cur = con.cursor() 
    cur.execute("INSERT INTO dhtReadings VALUES(datetime('now'), 30.5, 26)")
    #cur.execute("INSERT INTO dhtReadings VALUES(datetime('now'), 25.8, 40)")
    #cur.execute("INSERT INTO dhtReadings VALUES(datetime('now'), 19.3, 20)")