import argparse 
import os
from construct import *

#Fungsi untuk meload data csv permainan dari parent folder save kedalam program

#KAMUS LOKAL
#args.load, nama = string
#csv1, csv2, csv3 = string
#user, password, role, nama, deskripsi, id, pembuat, pasir, batu, air = list 
#total_pasir, total_batu, total_air = integer

#Algoritma
def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("load", help="Masukan nama folder yang ingin di load!",nargs='?')
    args = parser.parse_args()
    if args.load is None: #Jika nama folder kosong
        print()
        print("Tidak ada nama folder yang diberikan!")
        return None,None,None,None,None,None,None,None,None,None,None,None,None
    
    elif os.path.isdir("./save/" + args.load) == False : #Jika tidak ada folder di save, maka akan bernilai false
        nama = args.load
        args.load = "./save/" + args.load
        print()
        print(f'Folder "{nama}" tidak ditemukan.')
        return None,None,None,None,None,None,None,None,None,None,None,None,None

    elif os.path.isdir("./save/" + args.load) == True: #Jika folder ada, maka akan diload data csv dari folder tsb
        args.load = "./save/" + args.load
        print()
        print("Loading . . .")
        print('Selamat datang di program “Manajerial Candi”')

        csv1 = args.load + '/user.csv'
        users(csv1)

        csv2 = args.load + '/bahan_bangunan.csv'
        with open(csv2) as file:
            csv_bahan  = file.readlines()
        if length(csv_bahan) == 1:
            initial = "nama;deskripsi;jumlah\n" + "pasir;dari pantai;0\n" + "batu;dari gunung;0 \n" + "air;dari sungai;0"
            with open(csv2, 'w') as f:
                f.write(initial)
        bahan(csv2)

        csv3 = args.load + '/candi.csv'
        with open(csv3) as file:
            csv_candi = file.readlines()
        if length(csv_candi) == 1:
            id = [0]
            pembuat = ['none']
            pasir = [0]
            batu = [0]
            air = [0]
        else:
            candi(csv3)
            #candi.csv
            id = (candi(csv3)[0])
            pembuat = (candi(csv3)[1])
            pasir = (candi(csv3)[2])
            batu = (candi(csv3)[3])
            air = (candi(csv3)[4])

        #user
        user = (users(csv1)[0])
        password = (users(csv1)[1])
        role = (users(csv1)[2])

        #Bahan_Bangunan.csv
        nama = (bahan(csv2)[0])
        deskripsi = (bahan(csv2)[1])
        total_pasir = (bahan(csv2)[2][0])
        total_batu = (bahan(csv2)[2][1])
        total_air = (bahan(csv2)[2][2])

        return user, password, role, nama, deskripsi, id, pembuat, pasir, batu, air, total_pasir, total_batu, total_air
