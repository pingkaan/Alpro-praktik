dictMahasiswa =  {
    "nim" : "5220411001",
    "nama" : "rismawan",
    "prodi" : "informatika",
    "alamat" : "yogyakarata"
}

dataMahasiswa = []

# 1.
print("Prodi : ", dictMahasiswa['prodi'])

# 2.
dictMahasiswa["hobi"] = "menghayal"
print("Data Mahasiswa = ", dictMahasiswa)

# 3.
del dictMahasiswa["alamat"]
print("Data Mahasiswa = ", dictMahasiswa)

# 4.
dictMahasiswa["alamat"] = "yogyakarta"
dataMahasiswa = [dictMahasiswa]
print("Data Mahasiswa = ", dataMahasiswa)

# 5.
dataMahasiswa.append({
    "nim" : "5220411002",
    "nama" : "oktavia",
    "prodi" : "arsitektur",
    "hobi" : "menyanyi"
})
print("Data Mahasiswa = ", dataMahasiswa)


# 6.
dataMahasiswa[0]["hobi"] = "coding"
print("Data Mahasiswa = ", dataMahasiswa)

# 7.
print("NIM ", dataMahasiswa[0]["nim"], "dengan nama", dataMahasiswa[0]["nama"])
print("NIM ", dataMahasiswa[1]["nim"], "dengan nama", dataMahasiswa[1]["nama"])
