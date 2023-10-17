from mysql.connector import Connect, Error

def koneksi() :
    konekdidb = None
    try : 
        koneksidb = Connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "isna_rafif"
            )
        print("Berhasil")
    except Error as e :
        print(e)
    return koneksidb

def menu(conn) :
    print("1. Pendaftaran")
    print("2. Daftar Peserta")
    print("3. ")