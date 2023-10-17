# kerangka tugas
budget = 100000
jumlah = 1
genre1 = "romance"
genre2 = "action"
genre3 = "angst"
genre4 = "fanfiction"
penulis1 = "tereliye"
penulis2 = "tenderlova" 

budgetPembelian = int(input("Budget yang dimiliki = "))
jumlahNovel = int(input("Jumlah novel yang diinginkan = "))
genre = input("Genre buku yang diinginkan = ")
penulis = input("Penulis yang diinginkan = ")

if budgetPembelian >= budget :
    print(f"Jumlah buku yang diinginkan = ",jumlahNovel)
    if jumlahNovel == jumlah :
        print(f"Genre buku yang diinginkan = ",genre)
        if genre == genre1 :
            print(f"Penulis yang diinginkan = ",penulis)
            if penulis == penulis1 :
                print(f"Belilah 1 novel bergenre romance dari Tereliye")
            else : 
                print(f"Belilah 1 novel bergenre romance dari Tenderlova")
        elif genre == genre2 :
            print(f"Belilah 1 novel bergenre action dari Tereliye")
        elif genre == genre3 :
            print(f"Penulis yang diinginkan = ",penulis)
            if penulis == penulis1 :
                print(f"Belilah 1 novel bergenre angst dari Tereliye")
            else : 
                print(f"Belilah 1 novel bergenre angst dari Tenderlova")
        elif genre == genre4 :
            print(f"Belilah 1 novel bergenre fanfiction dari Tenderlova")
        else :
            print(f"Belilah 1 novel bergenre apapun dari Tereliye atau Tenderlova")
    else :
        print(f"Genre buku yang diinginkan = ",genre)
        if genre == genre1 :
            print(f"Penulis yang diinginkan = ",penulis)
            if penulis == penulis1 :
                print(f"Belilah beberapa novel bergenre romance dari Tereliye")
            else : 
                print(f"Belilah beberapa novel bergenre romance dari Tenderlova")
        elif genre == genre2 :
            print(f"Belilah beberapa novel bergenre action dari Tereliye")
        elif genre == genre3 :
            print(f"Penulis yang diinginkan = ",penulis)
            if penulis == penulis1 :
                print(f"Belilah beberapa novel bergenre angst dari Tereliye")
            else : 
                print(f"Belilah beberapa novel bergenre angst dari Tenderlova")
        elif genre == genre4 :
            print(f"Belilah beberapa novel bergenre fanfiction dari Tenderlova")
        else :
            print(f"Belilah beberapa novel bergenre apapun dari Tereliye atau Tenderlova")
else :
    print(f"Genre buku yang diinginkan = ",genre)
    if genre == genre1 :
        print(f"Penulis yang diinginkan = ",penulis)
        if penulis == penulis1 :
            print(f"Belilah 1 novel bergenre romance dari Tereliye")
        else : 
            print(f"Belilah 1 novel bergenre romance dari Tenderlova")
    elif genre == genre2 :
        print(f"Belilah 1 novel bergenre action dari Tereliye")
    elif genre == genre3 :
        print(f"Penulis yang diinginkan = ",penulis)
        if penulis == penulis1 :
            print(f"Belilah 1 novel bergenre angst dari Tereliye")
        else : 
            print(f"Belilah 1 novel bergenre angst dari Tenderlova")
    elif genre == genre4 :
        print(f"Belilah 1 novel bergenre fanfiction dari Tenderlova")
    else :
        print(f"Belilah 1 novel bergenre apapun dari Tereliye dan Tenderlova")
        