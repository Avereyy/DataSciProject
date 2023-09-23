from construct import *
from load import *
import login ; import logout ; import exit ; import logout ; import help
import summonjin ; import kumpul ; import hapusjin ; import save ; import ubahjin ; import bangun ; import hancur
import batchkumpul ; import batchbangun ; import laporanjin ; import laporancandi ; import ayamberkokok

#Prosedur utama program untuk mengakses fungsi komplemen yang ada untuk menjalankan permainan

#KAMUS GLOBAL
#user, password, role, nama, deskripsi, id, pembuat, pasir, batu, air = list 
#total_pasir, total_batu, total_air = integer
#username, cekrole, opsi = string
#status = bool

#Algoritma
if __name__ == "__main__":
    user, password, role, nama, deskripsi, id, pembuat, pasir, batu, air, total_pasir, total_batu, total_air = Main()
    #cek jika data yang di load merupakan data bukan None
    if user != None and password != None and role != None and nama != None and deskripsi != None and id != None and pembuat != None and total_pasir != None and total_batu != None and total_air != None:
        id, pembuat, pasir, batu, air = checkKosong(id, pembuat, pasir, batu, air)

        username = "pass" #Variabel digunakan untuk mengakses opsi pilihan dibawah
        cekrole = "none"
        status = True
        while status == True: #Jika bernilai False, maka program akan berhenti

            #Dibawah berisikan beberapa opsi yang dapat diakses per role
            opsi = input(">>> ")
            if opsi == "help":
                help.help(cekrole)

            elif opsi == "login":
                if username != "pass":
                    print(f'Login gagal!\nAnda telah login dengan username {username}, silahkan lakukan "logout" sebelum melakukan login kembali')
                else:
                    (username, cekrole) = login.login(user, password,role)
                
            elif opsi == "logout":
                if username == "pass":
                    print("Logout gagal! Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
                else:
                    (username, cekrole) = logout.logout()

            elif opsi == "summonjin":
                if cekrole == "bandung_bondowoso":
                    user, password, role = summonjin.summonjin(user, password, role)

            elif opsi == "hapusjin":
                if cekrole == "bandung_bondowoso":
                    user,password,role,id,pembuat,pasir,batu,air = hapusjin.hapusjin(user,password,role,id,pembuat,pasir,batu,air)

            elif opsi == "ubahjin":
                if cekrole == "bandung_bondowoso":
                    user, password, role == ubahjin.ubahjin(user, password, role)

            elif opsi == "kumpul":
                if cekrole == "jin_pengumpul":
                    total_pasir, total_batu, total_air = kumpul.kumpul(total_pasir, total_batu, total_air)

            elif opsi == "batchkumpul":
                if cekrole == "bandung_bondowoso":
                    total_pasir, total_batu, total_air = batchkumpul.batchkumpul(role, total_pasir, total_batu, total_air)


            elif opsi == "hancurkancandi":
                if cekrole == "roro_jonggrang":
                    id, pembuat, pasir, batu, air = hancur.hancur(id, pembuat, pasir, batu, air)


            elif opsi == "bangun":
                if cekrole == "jin_pembangun":
                    id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air = bangun.bangun(id, pembuat, pasir, batu, air, total_pasir, total_batu, total_air,username)

            elif opsi == "batchbangun":
                if cekrole == "bandung_bondowoso":
                    id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air = batchbangun.batchbangun(user, role, id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air)
            
            elif opsi == "laporanjin":
                if cekrole == "bandung_bondowoso":
                    laporanjin.laporan(user, role, pembuat, total_pasir, total_batu, total_air, id, pasir, batu, air)
                elif cekrole != "bandung_bondowoso":
                    print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
            
            elif opsi == "laporancandi":
                if cekrole == "bandung_bondowoso":
                    laporancandi.laporancandi(id, pembuat, pasir, batu, air)
                elif cekrole != "bandung_bondowoso":
                    print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")

            elif opsi == "ayamberkokok":
                if cekrole == "roro_jonggrang":
                    status = ayamberkokok.ayamberkokok(pembuat, pasir, batu, air)
            elif opsi == "save":
                save.save(user,password,role,total_pasir,total_batu,total_air,id,pembuat,pasir,batu,air)

            elif opsi == "exit":
                status = exit.exit(user,password,role,total_pasir,total_batu,total_air,id,pembuat,pasir,batu,air) #True -> jalan, False -> keluar
