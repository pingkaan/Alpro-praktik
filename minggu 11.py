from mysql.connector import Connect, Error

def koneksi():
    koneksidb = None
    try :
        koneksidb = Connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "toko"
        )
        print("Berhasil Terkoneksi dengan Database!")
    except Error as e :
        print(e)
    return koneksidb

# koneksi()

def tampilData(conn) :
    query = "SELECT * FROM barang"

    with conn.cursor() as cur :
        cur.execute(query)
        result = cur.fetchall()
        for row in result :
            print(row)

# tampilData(koneksi())

# def tambahData(conn,data) :
#     query = "INSERT INTO barang(kode,nama_barang,harga) VALUE(%s, %s, %s)"

#     try :
#         with conn.cursor() as cur :
#             cur.execute(query,data)
#             conn.commit()
#             print("Barang Berhasil Ditambahkan!")
#     except Error as e :
#         print(e)

# dataBarang = ("GJ81", "Isolatip", 7000)
# tambahData(koneksi(),dataBarang)
tampilData(koneksi())

# def ubahData (conn,data) :
#     query = "UPDATE SET barang nama_barang=%s, harga=%s, WHERE kode_barang=%s"

#     try :
#         with conn.cursor() as cur :
#             cur.execute(query,data)
#             conn.commit()
#             print("Barang Berhasil Diubah!")
#     except Error as e :
#         print(e)

# ubahBarang = 