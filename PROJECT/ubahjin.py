from construct import *

#Fungsi untuk mengubah tipe jin yang ada di dalam data users

#KAMUS LOKAL
#username_jin, confirm, initial, final, new_tipe = string

#Algoritma
def ubahjin(user, password, role):
    username_jin = str(input("Masukkan username jin : "))
    for i in range(length(user)): #Cek unsername ada atau tidak
        if(username_jin == user[i]): #Jika ada langsung ubah jenis jin
            if(role[i] == "jin_pengumpul"):
                initial = "Pengumpul"
                final = "Pembangun"
                new_tipe = "jin_pembangun"
            if(role[i] == "jin_pembangun"):
                initial = "Pembangun"
                final = "Pengumpul"
                new_tipe = "jin_pengumpul"
            
            confirm = str(input("Jin ini bertipe "+str(initial)+". Yakin ingin mengubah ke tipe "+str(final)+" (Y/N)?")) #KOnfirmasi perubahan
            while(confirm != "Y" and confirm != "N"):
                print()
                print("Input tidak valid ulangi lagi!")
                confirm = str(input("Jin ini bertipe Pengumpul. Yakin ingin mengubah ke tipe Pembangun (Y/N)?"))
                print()
            if(confirm == "Y"):
                role[i] = str(new_tipe)
                print("Jin telah berhasil diubah.")
                return user, role, password
            else: #Confirm == "N"
                print("Tipe jin tidak jadi diubah.")
                return user, role, password
            
    print()
    print("Tidak ada jin dengan username tersebut.") #Jika tidak ada jin dengan nama yang dimasukan
    return user, role, password
