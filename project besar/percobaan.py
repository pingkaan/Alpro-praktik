import string
import random
import datetime
from mysql.connector import Connect, Error


# n = 10
# result = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
# print("" + str(result))

# x = datetime.datetime.now()
# print(x)

def koneksi():
    koneksidb = None
    try :
        koneksidb = Connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "percobaan_db"
            )
    except Error as e :
        print(e)
    return koneksidb

def masukkanKeranjang(conn) :
    inputan = input("\nMasukkan judul buku : ")
    query = "INSERT INTO tbl_keranjang SELECT * FROM tbl_daftar_buku WHERE judul LIKE %s OR pengarang LIKE %s"
    val = ("%{}%".format(inputan), "%{}%".format(inputan))
    cursor = conn.cursor()
    cursor.execute(query, val)
    result1 = conn.commit()
    result2 = cursor.fetchall()
    result = (result1, result2)
    print("\nBerhasil memasukkan buku ke dalam keranjang!\n")

masukkanKeranjang(koneksi())