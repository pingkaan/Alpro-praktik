from mysql.connector import Connect, Error
import hashlib
import os
from prettytable import prettytable
import pandas as pd

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

def cariBuku(conn):
    print("===================================")
    print("       CARI DATA MAHASISWA         ")
    print("===================================")
    keyword = input("Masukkan keyword: ")
    cursor = conn.cursor(dictionary=True)
    cekbuku = "SELECT * FROM daftar_buku WHERE judul LIKE %s OR pengarang LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(cekbuku, val)
    hasilna = cursor.fetchall()
    if cursor.rowcount < 1:
        print("Tidak dapat menemukan buku dengan keyword {}".format(keyword))
    else:
        print("\nHasil Pencarian Buku dengan keyword {}".format(keyword))
        print("Ditemukan {} data\n".format(cursor.rowcount))
        tabel2 = prettytable()
        tabel2.field_names = ["ISBN", "JUDUL", "PENERBIT", "PENGARANG", "JUMLAH HALAMAN", "JUMLAH STOK", "TAHUN TERBIT"]
        for i in hasilna:
            tabel2.add_row([i['id_buku'], i['judul'], i['penerbit'], i['pengarang'], i['jumlah_halaman'], i['jumlah_stok'], i['tahun_terbit']])
        print(tabel2)
        tabel2.clear_rows()

def kop() :
    print("=====================================")
    print("         Selamat Datang di           ")
    print("          Da-Fi Bookstore            ")
    print("=====================================")

def menu(conn) :
    while True :
        os.system('cls')
        kop()
        print("1. Cari Buku")
        print("2. Keranjang")
        print("3. ")
        print("0. Keluar")
        pilihanMenu = int(input("\nPilih Menu : "))
        if pilihanMenu == 1 :
            cariBuku(conn)
        elif pilihanMenu == 2 :
            keranjang()
        elif pilihanMenu == 3 :
            pembayaran()
        elif pilihanMenu == 0 :
            print("=========================================")
            print("     Terimakasih Telah Berbelanja        ")
            print("          di Da-Fi Bookstore             ")
            print("=========================================")
            break
        else :
            print("Mohon masukkan pilihan menu yang sesuai!")
        os.system('pause')
    print('Terimakasih')

def login(conn):
    print("===================================")
    print("   LOGIN APLIKASI DATA MAHASISWA   ")
    print("===================================")
    username = input("Username: ")
    password = input("Password: ")
    pwd = hashlib.md5(password.encode())
    pwdna = pwd.hexdigest()

    cursor = conn.cursor()
    sql = "SELECT * FROM tbl_user WHERE username=%s AND password=%s"
    val = (username, pwdna)
    cursor.execute(sql, val)
    hasil = cursor.fetchall()

    if cursor.rowcount > 0:
        os.system("cls")
        print("\nHallo {}, anda berhasil login. Silahkan pilih menu!".format(username))
        while True:
            menu(conn)
    else:
        print("Username atau Password tidak ditemukan!\n")
        login(conn)

login(koneksi())