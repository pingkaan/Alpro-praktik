# membeli rumah
statusMenikah = "Sudah"
pendapatan1 = 80000
pendapatan2 = 40000
jumlahKeluarga = int(input("Jumlah anggota keluarga = "))
status_Menikah = input("Status pernikahan = ")
pendapatan = int(input("Pendapatan yang didapatkan = "))

if jumlahKeluarga > 3 :
    print(f"Status pernikahan = ",status_Menikah)
    if status_Menikah == statusMenikah :
        print(f"Maka belilah rumah 3BHK")
    else :
        print(f"Pendapatan yang didapatkan = ",pendapatan)
        if pendapatan > pendapatan2 :
            print(f"Maka belilah rumah 2BHK")
        else :
            print(f"Maka belilah rumah 1BHK")

if jumlahKeluarga <= 3 :
    print(f"Pendapatan yang didapatkan = ",pendapatan)
    if pendapatan > pendapatan1 :
        print(f"Maka belilah rumah 4BHK")
    else :
        print(f"Status pernikahan = ",status_Menikah)
        if status_Menikah == statusMenikah :
            print(f"Maka belilah rumah 3BHK")
        else :
            print(f"Maka belilah rumah 2BHK")
