#1.
def tambah(A,B) :
    C =[0, 0, 0,]
    for i in range(len(A)) :
        C[i] = A[i] + B[i]
    return print(C)

A = [1, 2, 3]
B = [4, 5, 6]
tambah(A,B)

#2.
def kurang(mA,mB) :
    mC = [[0, 0, 0], 
    [0, 0, 0]]
    for i in range(len(mA)) :
        for j in range(len(mA[0])) :
            mC[i][j] = mA[i][j] - mB[i][j]
    return print(mC)

mA = [[1, 2, 3], [4, 2, -2]]
mB = [[-5, 1, 3], [4, -3, -1]]
kurang(mA,mB)

import numpy as np
ma = np.array(mA)
mb = np.array(mB)
mc = ma - mb
print(mc)



# 1.
a = np.array(A)
b = np.array(B)
c = a - b
print(c)
print("\t")

# 2.
mc1 = ma * mb
print(mc1)
print("\t")

# 3.
mbT = mb.transpose()
print(mbT)
print("\t")

# 4.
print(mbT.shape)
print("\t")

# 5.
print(ma.dot(mbT))
print("\t")

# 6.
ma,mbT = ma.flatten(), mbT.flatten()
print(ma,mbT)
vc = np.concatenate((ma,mbT))
print(vc)
print("\t")

# 7.
vcMin = np.min((vc))
print(vcMin)
print(vc.min())

vcMax = np.max((vc))
print(vcMax)
print(vc.max())

vcAvg = np.average((vc))
print(vcAvg)

vcSD = np.std(vc)
print(vcSD)
print(vc.std())

# 8.
vcEnd = np.reshape(vc,(4,3))
print(vcEnd)