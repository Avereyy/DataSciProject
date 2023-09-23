from construct import *

#Prosedur untuk menghapus jin dari daftar user

#KAMUS LOKAL
#user, password, role = list
#uname, confirm = string

#Algoritma
def hapusjin(list_user, list_pass, list_role,id,pembuat,pasir,batu,air):
    uname = input("Masukkan username jin: ") 
    user = [" "] ; password = [" "] ; role = [" "] #Sama seperti hancurkancandi, trdapat array sementara untuk mengisi ulang data user
    for i in range(length(list_user)):
        if uname == list_user[i] and (list_role[i] == "jin_pengumpul" or list_role[i] == 'jin_pembangun'):
            confirm = str(input("Apakah anda yakin ingin menghapus jin dengan username "+str(uname)+" (Y/N)? "))
            while(confirm != "Y" and confirm != "N"):
                print()
                print("Input tidak valid ulangi lagi!")
                confirm = str(input("Apakah anda yakin ingin menghapus jin dengan username "+str(uname)+" (Y/N)? "))
                print()

            if confirm == "Y": #Mengisi data user tanpa jin yang dihapus
                for i in range(length(list_user)):
                    if uname != list_user[i]:
                        user = xappend(user, [str(list_user[i])])
                        password = xappend(password, [str(list_pass[i])])
                        role = xappend(role, [str(list_role[i])])
                for i in range(length(id)): #Jika sesuai, maka candi dengan pembuat user tersebut akan menjadi 0;none;0;0;0 (hancur)
                    if uname == pembuat[i]:
                        id[i] = 0
                        pembuat[i] = 'none'
                        pasir[i] = 0
                        batu[i] = 0
                        air[i] = 0

                    
                print("Jin telah berhasil dihapus dari alam gaib.")
                return user, password, role, id, pembuat, pasir, batu, air
            else: #confirm == "N"

                print("Jin gagal dihapus dari alam gaib.")
                return list_user, list_pass, list_role, id, pembuat, pasir, batu, air

    print()
    print("Tidak ada jin dengan username tersebut.") #Jika input tidak valid
    return list_user, list_pass, list_role, id, pembuat, pasir, batu, air