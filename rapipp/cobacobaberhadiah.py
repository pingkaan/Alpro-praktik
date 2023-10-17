from mysql import connector

connect = connector.connect(
    host="localhost",
    user="root",
    password="",
    database="praktikum_alpro_sabtu"
)

cursor = connect.cursor()

cursor.execute("""
               INSERT INTO mahasiswa VALUES()
               """
               )