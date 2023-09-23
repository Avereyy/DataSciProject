from construct import *

#Fungsi untuk melakukan login pada menu utama permainan

#KAMUS LOKAL
#username, passw = string
#num, count = integer

#Algoritma
def login(user, password,role):
    num  = length(user) #Menerima input username dan pw
    username = input("Username: ")
    passw = input("Password: ")
    count = 0
    for i in range(num):
        if username != user[i]:
            count += 1
            if count == length(user): #Jika tidak ada dalam daftar user, tidak akan bisa masuk program
                print("Username tidak terdaftar!")
                return("pass", "none")
        elif (username == user[i]) and (passw == password[i]): #Jika masuk, maka akan memberikan username dan role sesuai user
            print(f"Selamat datang, {username}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.")
            return(username, role[i]) 
        elif (username == user[i]) and (passw != password[i]): #Jika password salah, tidak akan me return apa"
            print("Password salah!")
            return("pass", "none")