import pandas as pd

# membuat data frame
data = [['Raehan', 85], ['Bobby', 90], ['Johana', 80]]
dataFrame = pd.DataFrame(data, columns=['Nama', 'Nilai1'])
print(dataFrame)

# menabahkan kolom (series)
dataFrame["Nilai2"] = pd.Series([70,85,70])
print(dataFrame)

#tambahkan kolom rata rata dan isi rata ratany
dataFrame["Rata-Rata"] = (dataFrame["Nilai1"]+dataFrame["Nilai2"])/2
print(dataFrame)

# dataFrame["Nilai2"][2] = [90]
# print(dataFrame)

# # baca data dari file
# dataPenilaian = pd.read_excel("rekap_penilaian.xlsx")
# print(dataPenilaian)

# tambahkan kolom fullname hasil gabungan dari first name dan last name
# dataPenilaian["Fullname"] = dataPenilaian["First Name"]+" "+dataPenilaian["Last Name"]
# print(dataPenilaian)