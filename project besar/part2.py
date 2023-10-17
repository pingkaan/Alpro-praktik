def cariBuku(conn):
    query = "SELECT * FROM barang"

    with conn.cursor() as cur :
        cur.execute(query)
        result = cur.fetchall()
        for row in result :
            print(row)

import os
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
        print("---------------------------------------------------------")
        print("             Terimakasih Telah Berbelanja                ")
        print("                  di Da-Fi Bookstore                     ")
        print("---------------------------------------------------------")
        break
    else :
        print("Mohon masukkan pilihan menu yang sesuai!")
    os.system('pause')
print('Terimakasih')