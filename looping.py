angka = 1
while angka < 10 :
    print(angka)
    angka = angka + 1
print(angka)

data = [12,"Zaka", 40, 64, "Yongga"]

# 1. Tampilan item ke 2
print(data[1])

# 2. Tampilkan semua item di dalam list data
for item in data :
    print(item)

# 3. Tampilkan item terakhir
print(data[4])

# 4. Tampilkan item yang string dan yang integer
print(f"Tipe data string = ",data[1], data[4])
print(f"Tipe data integer = ",data[0], data[2], data[3])

for item in data :
    print(type(item))

# 5. Tampilkan hasil penjumlahan semua angka
print("Hasil = ",data[0]+data[2]+data[3])
