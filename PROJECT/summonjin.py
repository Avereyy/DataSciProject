from construct import *

#Fungsi untuk menambahkan jin ke dalam data users

#KAMUS LOKAL
#username_jin, jenis_jin, password_jin = string
#i = integer
#isPassValid = bool

#Algoritma
def summonjin(user, password, role):
    if length(user) >= 102: #Jika sudahh maksimal maka tidak akan menjalankan apa"
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        return user, password, role
    else: #Jika belum penuh maka akan dijalankan seperti dibawah
        print("Jenis jin yang dapat dipanggil: ") 
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")
        print()
        jenis_jin = str(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        while(jenis_jin != str(1) and jenis_jin != str(2) ):
            print()
            print("Tidak ada jenis jin bernomor "+str(jenis_jin)+"!")
            print()
            jenis_jin = str(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
       
        print() #Menetukan jenis jin yang disummon
        if(jenis_jin == '1'):
            role = xappend(role, ['jin_pengumpul'])
            print('Memilih jin "Pengumpul".')
        elif(jenis_jin == '2'):
            role = xappend(role, ['jin_pembangun'])
            print('Memilih jin "Pembangun".')
        print()
        username_jin = input("Masukkan username jin: ")
        i = 0
        while(i < length(user)): #Cek jika username belum diambil
            if(username_jin == user[i]):
                print()
                print(f'Username "{str(username_jin)}" sudah diambil!')
                print()
                username_jin = input("Masukkan username jin: ")
                i = 0
            else:
                i = i + 1
    
        #Jika username sudah valid, maka akan ditanyakan password
        i = 0
        user = xappend(user, [str(username_jin)])
        #Memasukan user kedalam array user
    
        password_jin = input("Masukkan password jin: ")
        isPassValid = False
        while(isPassValid == False):
            if(length(password_jin) > 25 or length(password_jin) < 5):
                print()
                print("Password panjangnya harus 5-25 karakter!")
                print()
                password_jin = input("Masukkan password jin: ")
                print()
            else: #Jika password sudah valid, maka akan dimasukan ke array password
                isPassValid = True
        password = xappend(password, [str(password_jin)])
        print()
        print("Mengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")
        print()
        print("Jin "+str(username_jin)+" berhasil dipanggil!")
        return user, password, role