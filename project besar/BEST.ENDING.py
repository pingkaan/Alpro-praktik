from mysql.connector import Connect, Error
import hashlib
import os
import pandas as pd
import string
import random
import datetime

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

def kop() :
    print("=====================================")
    print("         Selamat Datang di           ")
    print("          Da-Fi Bookstore            ")
    print("=====================================")

def keluar() :
    os.system('cls')
    print("=========================================")
    print("     Terimakasih Telah Berbelanja        ")
    print("          di Da-Fi Bookstore             ")
    print("=========================================")

def pembayaran(conn) :
    n = 10
    idPembayaran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
    date = datetime.datetime.now()
    idBuku = input("Masukkan ID buku yang akan dibeli : ")
    jumlah = input("Masukkan jumlah buku yang diinginkan : ")
    print("1. COD (Bayar di Tempat)")
    print("2. Transfer Bank")
    metode = input("Pilih metode pembayaran : ")
    ket = ("Pesanan Sedang Diproses")
    cursor = conn.cursor()
    query = "INSERT INTO pembayaran (id_pembayaran, id_buku, tgl_keluar, jumlah, metode, keterangan) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (idPembayaran, idBuku, date, jumlah, metode, ket)
    cursor.execute(query, val)
    result = conn.commit()

    if metode == 'transfer bank' :
        query = "SELECT * FROM pembayaran"
        with conn.cursor() as cur :
            cur.execute(query)
            result = cur.fetchall()
            hasil = pd.DataFrame(result, columns=["KODE PEMESANAN", "ID BUKU", "WAKTU PEMBELIAN", "JUMLAH", "METODE PEMBAYARAN", "KETERANGAN"])
            print("\n",hasil)
            print("\nSilakan lakukan pembayaran dengan menggunakan kode pemesanan!")
            print("Terimakasih telah melakukan pemesanan!\n")
    else :
        query = "SELECT * FROM pembayaran"
        with conn.cursor() as cur :
            cur.execute(query)
            result = cur.fetchall()
            hasil = pd.DataFrame(result, columns=["KODE PEMESANAN", "ID BUKU", "WAKTU PEMBELIAN", "JUMLAH", "METODE PEMBAYARAN", "KETERANGAN"])
            print("\n",hasil)
            print("\nSilakan menunggu dan lakukan pembayaran saat barang sudah sampai!")
            print("Terimakasih telah melakukan pemesanan\n")

def cariBuku(conn) :
    kop()
    print("\t \t>> Cari Buku")
    print("\t \t---------------------")
    keyword = input("\nKetik judul atau nama pengarang : ")
    cursor = conn.cursor()
    query = "SELECT * FROM tbl_daftar_buku WHERE judul LIKE %s OR pengarang LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(query, val)
    result = cursor.fetchall()
    hasil = pd.DataFrame(result, columns=["ID", "JUDUL", "PENERBIT", "PENGARANG", "HARGA", "JUMLAH STOK"])
    if cursor.rowcount < 1 :
        print("\nMohon maaf, buku yang Anda cari tidak tersedia!\n")
        os.system('pause')
        os.system('cls')
        cariBuku(koneksi())
    else :
        print("\nBuku yang tersedia :")
        print(hasil)
        print("\n")
        print("\t \t>> Pilihan Menu")
        print("\t \t---------------------")
        print("1. Beli Buku")
        print("2. Masukkan Keranjang")
        print("0. Kembali")
        pilihMenu = str(input("\nPilih Menu : "))

        os.system('cls')

        if pilihMenu == '1' :
            kop()
            print("\t \t>> Pembayaran")
            print("\t \t---------------------\n")
            print(hasil)
            print("\n")
            pembayaran(koneksi())
            os.system('pause')
            os.system('cls')
        elif pilihMenu == '2' :
            kop()
            print(hasil)
            masukkanKeranjang(koneksi())
            os.system('pause')
            os.system('cls')
        elif pilihMenu == "0":
            menu(koneksi())
        else:
            print("Tidak ditemukan menu {} di program ini!".format(pilihMenu))
            os.system('pause')
            os.system('cls')

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

def keranjang(conn) :
    os.system('cls')
    kop()
    print("\t \t>> Keranjang")
    print("\t \t---------------------\n")
    cursor = conn.cursor()
    query = "SELECT * FROM tbl_keranjang"
    cursor.execute(query)
    result = cursor.fetchall()
    hasil = pd.DataFrame(result, columns=["ID", "JUDUL", "PENERBIT", "PENGARANG", "HARGA", "JUMLAH STOK"])
    print(hasil)
    pilihan = input("\nApakah Anda akan melakukan pembelian? (yes or no) : ")
    if pilihan == 'yes' :
        inputan = input("\nMasukkan judul buku : ")
        pembayaran(koneksi())
        cursor = conn.cursor()
        query = "DELETE FROM tbl_keranjang WHERE judul LIKE %s OR pengarang LIKE %s"
        val = ("%{}%".format(inputan), "%{}%".format(inputan))
        cursor.execute(query, val)
        conn.commit()
        os.system('pause')
        os.system('cls')
    else :
        os.system('cls')
        menu(koneksi())

def pesanan(conn) :
    os.system('cls')
    kop()
    print("\t \t>> Pesanan")
    print("\t \t---------------------\n")
    query = "SELECT * FROM pembayaran"
    with conn.cursor() as cur :
        cur.execute(query)
        result = cur.fetchall()
        hasil = pd.DataFrame(result, columns=["KODE PEMESANAN", "ID BUKU", "WAKTU PEMBELIAN", "JUMLAH", "METODE PEMBAYARAN", "KETERANGAN"])
        print(hasil)
        print("\nSilakan menunggu, pesanan sedang diproses!\n")
        os.system('pause')
        os.system('cls')

def menu(conn) :
    kop()
    print("\t \t>> Menu")
    print("\t \t---------------------\n")
    print("1. Cari Buku")
    print("2. Keranjang")
    print("3. Pesanan")
    print("0. Keluar")
    print("-------------------------------------")
    pilihMenu = str(input("Pilih Menu: "))

    os.system("cls")

    if pilihMenu == "1":
        cariBuku(koneksi())
    elif pilihMenu == "2":
        keranjang(koneksi())
    elif pilihMenu == "3":
        pesanan(koneksi())
    elif pilihMenu == "0":
        keluar()
        exit()
    else:
        print("Tidak ditemukan menu {} di program ini!\n".format(pilihMenu))
        os.system('pause')
        os.system('cls')


def login_aplikasi(conn):
    kop()
    print("Silakan Login!\n")
    username = input("Username : ")
    password = input("Password : ")
    pwd = hashlib.md5(password.encode())
    pwdna = pwd.hexdigest()

    cursor = conn.cursor()
    sql = "SELECT * FROM tbl_user WHERE username=%s AND password=%s"
    val = (username, pwdna)
    cursor.execute(sql, val)
    hasil = cursor.fetchall()

    if cursor.rowcount > 0:
        os.system('cls')
        kop()
        print("\nHallo {}, Anda berhasil login. Silahkan pilih menu!\n".format(username))
        os.system('pause')
        os.system('cls')
        while True:
            menu(conn)
    else:
        print("\nUsername atau Password tidak ditemukan. Silakan login lagi!\n")
        os.system('pause')
        os.system('cls')
        login_aplikasi(conn)

login_aplikasi(koneksi())