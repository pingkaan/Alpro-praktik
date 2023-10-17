def tambah(A,B):
    D = [0,0,0]
    for i in range(len(A)):
        D[i] = A[i] + B[i]
    return print(D)
print("\t")

def kurang(mA,mB):
    mC = [0,0,0], [0,0,0]
    for i in range(len(mA)):
        for j in range(len(mA[0])):
            mC[i][j] = mA[i][j] - mB[i][j]
    return print(mC)
print("\t")

A = [1, 2, 3]
B = [4, 5, 6]
tambah(A,B)

mA = [[1, 2, 3],
      [4, 2, -2]]
mB = [[-5, 1, 3],
      [4, -3, -1]]
kurang(mA,mB)



import numpy as np

#matrikA = np.array(mA)
#matrikB = np.array(mB)
#atau
matrikA,matrikB = np.array(mA), np.array(mB)
matrikC = matrikA - matrikB
print(matrikC)
print("\t")

#Operasi matrik
import numpy as ab

matrikA1 = ab.array(A)
matrikB1 = ab.array(B)
#1. Tunjukkan hasil pengurangan A dengan B
print("nomor 1")
matrikC1 = matrikA1 - matrikB1
print(matrikC1)
print("\t")

#2. Tunjukkan hasil perkalian mA dengan mB
print("nomor 2")
matrikC2 = matrikA * matrikB
print(matrikC2)
print("\t")

#3. Balik matrik mB menjadi ordo 3x2 (transpose matrik)
print("nomor 3")
mB = matrikB.transpose()
print(mB)
print("\t")

#4. Tunjukkan ordo matrik mB
print("nomor 4")
print(mB.shape)
print("\t")

#5. Kerjakan soal nomor 2
print("nomor 5")
print(matrikA1.dot(mB))
print("\t")

#6. Buatlah vektor baris "vC" yang merupakan gabungan dari mA dan mB
print("nomor 6")
mA,mB = matrikA1.flatten(), matrikB.flatten()
print(mA,mB)
vC = np.concatenate((mA,mB))
print(vC)
#7. Hitunglah nilai terendah, tertinggi, rata-rata, dan standar deviasi dari vC
vC1 = np.min((vC))
#8. Ubah bentuk vektor vC menjadi matrik dengan ukuran 4x3  