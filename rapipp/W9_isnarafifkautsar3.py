#5220411196 - Isna Rafif Kautsar
#Dictionary

buku=dict(
    judul= " ",
    penulis= " ",
    harga= "",
    jumlah= " ",
    uang= " ",
    kembalian= " "
)
import datetime
now=datetime.datetime.now()

import os

def isidata():
    print("Mengisi data buku : ")
    x=str(input("Masukkan Judul Buku            : "))
    buku['judul']=x
    x=str(input('Masukkan Penulis Buku          : '))
    buku['penulis']=x
    x=int(input('Masukkan Harga Buku            : '))
    buku['harga']=x
    x=int(input('Masukkan Jumlah Halaman Buku   : '))
    buku['jumlah']=x
    print('Berhasil di Inputkan')

def cetak():
    print('Cetak Buku')
    print("---",now,'---')
    print("Judul Buku           : ",buku.get("judul"))
    print("Penulis              : ",buku.get("penulis"))
    print("Harga Buku           : ",buku.get("harga"))
    print("Jumlah Halaman Buku  : ",buku.get("jumlah"))

def ubahjudul():
    print('Ubah Data Buku')
    a=input('Masukkan Judul Buku yang Baru      : ')
    buku['judul']=a

def hapusbuku():
    print('Hapus Buku')
    b=input('Apakah Anda Ingin Menghapus Buku Ini? <Y/T> : ')
    if b=='Y':
        buku.clear()
        cetak()
        print("Buku Telah Dihapus")
    elif b=='T':
        print('Buku Tidak jadi Dihapus')
        cetak()
    else:
        print('Error')

def belibuku():
    print('Anda Membeli Buku')
    print(      'Harga Buku             : ',buku.get('harga'))
    x=int(input('Masukkan Uang Anda     : '))
    if x > buku["harga"]:
        kembalian= x-buku["harga"]
        print(  'Kembalian Anda         : ',kembalian)
    else:
        print('Uang anda Kurang, Tidak bisa Membeli')

lanjut=True
while True:
    os.system('cls')
    print("1. Isi Data Buku")
    print("2. Cetak Buku")
    print("3. Ubah Judul Buku")
    print("4. Hapus Buku")
    print("5. Beli Buku")
    print("0. Keluar")
    pilihan_menu=int(input("Pilih Menu : "))
    if pilihan_menu==1:
        isidata()
    if pilihan_menu==2:
        cetak()
    if pilihan_menu==3:
        ubahjudul()
    if pilihan_menu==4:
        hapusbuku()
    if pilihan_menu==5:
        belibuku()
    if pilihan_menu==0:
        print('Project selesai')
        break
    os.system('pause')
print('Terimakasih')