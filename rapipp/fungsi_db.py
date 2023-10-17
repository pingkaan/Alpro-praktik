def masukkan_data(dbs):
    nim = input("\nMasukkan NIM : ")
    nama = input("Masukkan Nama : ")
    umur = input("Masukkan Umur : ")
    val = (nim, nama, umur)
    cursor = dbs.cursor()
    sql = "INSERT INTO daftar_mhs (nim, nama, umur) VALUES (%s, %s, %s)"
    cursor.execute(sql, val)
    dbs.commit()
    print("\n{} Data berhasil disimpan".format(cursor.rowcount))
    
def tampilkan_data(dbs):
    print("\n")
    cursor = dbs.cursor()
    sql = "SELECT * FROM daftar_mhs"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in result:
            print(data)
            
def ubah_data(dbs):
    cursor = dbs.cursor()
    tampilkan_data(dbs)
    nim = input("\nPilih nim : ")
    nama = input("Masukkan nama baru : ")
    umur = input("Masukkan umur baru : ")
    
    sql = "UPDATE daftar_mhs SET nama=%s, umur=%s WHERE nim=%s"
    val = (nama, umur, nim)
    cursor.execute(sql, val)
    dbs.commit()
    print("{} Data berhasil diubah".format(cursor.rowcount))
    
def hapus_data(dbs):
    cursor = dbs.cursor()
    tampilkan_data(dbs)
    nim = input("\nPilih nim : ")
    sql = "DELETE FROM daftar_mhs WHERE nim=%s"
    val = (nim,)
    cursor.execute(sql, val)
    dbs.commit()
    print("{} Data berhasil dihapus".format(cursor.rowcount))