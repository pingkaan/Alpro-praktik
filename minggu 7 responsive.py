# Nama = Pingkan Putri Nazarina
# NPM = 5220411173
import random
import os
huruf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
hurufAcak = huruf[random.randrange(len(huruf))]

def menu() :
    print("--------------------------------------------------------------------")
    print("                     PERMAINAN TEBAK HURUF A-Z                      ")
    print("--------------------------------------------------------------------")
    print(huruf)

percobaan = 0
while True :
    tebakanBenar = hurufAcak
    menu()
    tebakan = input("Masukkan tebakan anda = ")
    percobaan +=1 
    tebakan1 = huruf.index(tebakanBenar)
    tebakan2 = huruf.index(tebakan)
    if tebakan2 == tebakan1 :
        print(f"Jawaban anda benar pada percobaan {percobaan}")
    elif tebakan2 > tebakan1 :
        print(f"Jawaban anda salah, huruf jawaban berada sebelum {huruf[tebakan2]} percobaan {percobaan}")
    elif tebakan2 < tebakan1 :
        print(f"Jawaban anda salah, huruf jawaban berada sesudah {huruf[tebakan2]} percobaan {percobaan}")

