n = 5;
for i in range(n) :
    for j in range(i) :
        print('* ',end="")
    print('')

for i in range(n,0,-1) :
    for j in range(i) :
        print('* ',end="")
    print('')

def Mobil():
    data_mobil = [['merk', 'CC', 'harga(juta)'],
            ['Toyota Etios', '125', '100'],
            ['Toyota Veloz', '150', '250'],
            ['Toyota Inova', '200', '300']]
    for kol in data_mobil[1:]:
        mobil_cc = kol[1]
        mobil_cc = int(mobil_cc)
        kol[1] = mobil_cc
    print(data_mobil)
    total_range = 0
    for row in data_mobil[1:]:
        mobil_cc = row[1]
        total_range += mobil_cc
        number_of_cars = len(data_mobil[1:])
    print(total_range / number_of_cars)
    for kol in data_mobil[1:]: 
        harga = kol[2]
        if harga > 100 :
        long_range_car_list.append(row)
    print(long_range_car_list)
