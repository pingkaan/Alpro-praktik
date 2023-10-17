import os



from mysql.connector import Connect, Error

def koneksi():
    koneksidb = None
    try :
        koneksidb = Connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "percobaan_db"
            )
        print("Silakan Login!")
    except Error as e :
        print(e)
    return koneksidb

# koneksi()

def kop() :
    print("-------------------------------------")
    print("         Selamat Datang di           ")
    print("          Da-Fi Bookstore            ")
    print("-------------------------------------")


def signUp(conn):
    try :
        username = input("\nMasukkan Username : ")
        password = input("Masukkan Password : ")
        val = (username, password)
        cursor = conn.cursor()
        sql = "INSERT INTO tabel_login (username, password) VALUES (%s, %s)"
        cursor.execute(sql, val)
        conn.commit()
        print("\nBerhasil Login. Selamat Berbelanja!\n".format(cursor.rowcount))
        os.system('pause')
        os.system('cls')
    except Error as e :
        print(e)

signUp(koneksi())

while True:
    os.system('cls')
    print("-----------------------------------------------------")
    print("                 Selamat Datang di                   ")
    print("                  Da-Fi Bookstore                    ")
    print("-----------------------------------------------------")
    print("1. Cari Buku")
    print("2. Keranjang")
    print("3. ")
    print("0. Keluar")
    pilihanMenu = int(input("\nPilih Menu : "))
    if pilihanMenu == 1 :
        cariBuku()
    elif pilihanMenu == 2 :
        cetak()
    elif pilihanMenu == 3 :
        ubahjudul()
    elif pilihanMenu == 0 :
        print("-------------------------------------------------")
        print("         Terimakasih Telah Berbelanja            ")
        print("              di Da-Fi Bookstore                 ")
        print("-------------------------------------------------")
        break
    else :
        print("Mohon masukkan pilihan menu yang sesuai!")
    os.system('pause')
print('Terimakasih')

# lanjut = True
# while  :
#     signUp(koneksi())
#     print("Selamat Berbelanja!")
#     break
#     os.system('cls')
#     os.system('pause')
#     print("-----------------------------------------------------")
#     print("                 Selamat Datang di                   ")
#     print("                  Da-Fi Bookstore                    ")
#     print("-----------------------------------------------------")
#     print("1. Cari Buku")
#     print("2. Keranjang")
#     print("3. Ubah Judul Buku")
#     print("4. Hapus Buku")
#     print("5. Beli Buku")
#     print("0. Keluar")
#     pilihan_menu = int(input("\nPilih Menu : "))

# def tampilData(conn) :
#     query = "SELECT * FROM login"

#     with conn.cursor() as cur :
#         cur.execute(query)
#         result = cur.fetchall()
#         for row in result :
#             print(row)

# tampilData(koneksi())