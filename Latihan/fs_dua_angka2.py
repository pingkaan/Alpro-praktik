def password():
    user = input("User-nya = ")
    passw = input('Password-nya = ')
    user_ = "User"
    password_ = "Admin"
    if user == user_ and passw == password_ :
        print('Username dan password sesuai')
    else :
        print('Password tidak sesuai')

