import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,2)

semester = [1,2,3,4,5,6]
ip = [3.98, 3.56, 3.20, 3.01, 2.97, 3.75]
warna = ["red", "cyan", "blue", "magenta", "yellow", "green"]

ax[0,0].set_title("Index Prestasi Mahasiswa")
ax[0,0].set_xlabel("Semester")
ax[0,0].set_ylabel("Nilai Indeks Prestasi")
ax[0,0].bar(semester,ip,color=warna)

prodi = ["Sistem Informasi", "Informatika", "Psikologi"]
jumlahMahasiswa = [145,438,186]

ax[0,1].set_title("Jumlah Mahasiswa per-Prodi")
ax[0,1].pie(jumlahMahasiswa, labels=prodi, autopct="%i Mahasiswa")

data = [100,53,84,64,72,73,73,45,86,50,60,58]
month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

ax[1,0].set_title("Penjualan Mobil Perbulan")
ax[1,0].plot(month,data,alpha=0.5)
ax[1,0].scatter(range(12),data,color="red")

plt.show()