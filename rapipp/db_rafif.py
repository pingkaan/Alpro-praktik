#5220411196 - Isna Rafif Kautsar

import mysql.connector

dbs = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

if dbs.is_connected():
    print("database sukses terhubung")
    
cursor = dbs.cursor()
cursor.execute("CREATE DATABASE dbs_rafif")

print("Database sukses dibuat")