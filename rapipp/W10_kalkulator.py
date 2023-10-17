#5220411196
#Isna Rafif Kautsar

import math

def tambah(bilangan1,bilangan2):
    bilangan1=int(input("Masukkan Bilangan 1 : "))
    bilangan2=int(input("Masukkan Bilangan 2 : "))
    tambah = bilangan1 + bilangan2
    print("Hasil = ",tambah(bilangan1,bilangan2))
    return tambah

def kurang(bilangan1,bilangan2):
    bilangan1=int(input("Masukkan Bilangan 1 : "))
    bilangan2=int(input("Masukkan Bilangan 2 : "))
    kurang = bilangan1 - bilangan2
    print("Hasil = ",kurang(bilangan1,bilangan2))
    return kurang

def kali(bilangan1,bilangan2):
    bilangan1=int(input("Masukkan Bilangan 1 : "))
    bilangan2=int(input("Masukkan Bilangan 2 : "))
    kali = bilangan1 * bilangan2
    print("Hasil = ",kali(bilangan1,bilangan2))
    return kali
    
def bagi(bilangan1,bilangan2):
    bilangan1=int(input("Masukkan Bilangan 1 : "))
    bilangan2=int(input("Masukkan Bilangan 2 : "))
    bagi = bilangan1 / bilangan2
    print("Hasil = ",bagi(bilangan1,bilangan2))
    return bagi
    
def pangkat(bilangan1,bilangan2):
    bilangan1=int(input("Masukkan Bilangan 1 : "))
    bilangan2=int(input("Masukkan Bilangan 2 : "))
    pangkat = bilangan1 ** bilangan2
    print("Hasil = ",pangkat(bilangan1,bilangan2))
    return pangkat