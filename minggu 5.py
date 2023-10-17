def cetak_mhsw(nama,prodi,umur=18):
    print("Nama : ",nama);
    print("Umur : ",umur);
    print("Prodi : ",prodi);
    return;
# parameter tidak diisi semua
print("Tanpa memakai default argument : ")
cetak_mhsw(nama="Nino", umur=50, prodi="informatika")
print("\n")
# parameter tidak diisi semua
print("Memakai default argument : ")
cetak_mhsw(prodi="Tenik Informatika", nama="Nino")

