import matplotlib.pyplot as plt

semester = [1,2,3,4,5,6]
ip = [3.98,3.56,3.20,3.01,2.97,3.75]
prodi = ["Sistem Informasi", "Informatika","Psikologi"]
JumlahMahasiwa = [145,438,186]
warna = ["brown","black","gray","navy"]

fig,ax = plt.subplots(1,2)

ax[0].set_title("indeks prestasi persemester")
ax[0].set_xlabel("semester")
ax[0].set_ylabel("nilai indeks prestasi")
ax[0].bar(semester,ip,color=warna)


ax[1].set_title("Jumlah mahasiswa")
ax[1].pie(JumlahMahasiwa,labels=prodi,autopct="%i Mahasiswa")

plt.show()