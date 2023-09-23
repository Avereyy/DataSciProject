import save

#Fungsi untuk keluar dari program yang sedang jalan

#KAMUS LOKAL
#cek = bool
#ans = string

#Algoritma
def exit(user,password,role,total_pasir,total_batu,total_air,id,pembuat,pasir,batu,air):
    cek = True
    while cek == True:
        ans = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if (ans == "y") or (ans == "Y"):
            cek = False
            save.save(user,password,role,total_pasir,total_batu,total_air,id,pembuat,pasir,batu,air)
            return False #True akan membuat main() terus jalan

        elif (ans == "n") or (ans == "N"):
            cek = False
            return False #False akan mengembalikan nilai status di main dan langsung keluar dari program