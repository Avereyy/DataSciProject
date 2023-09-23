from construct import *
import os

#Fungsi untuk menyimpan data permainan ke dalam csv yang ada / belum ada di parent folder

#KAMUS LOKAL
#path1, path2, path3 = string
#foldername, folder = string

#Algoritma
def save(user,password, role, total_pasir, total_batu, total_air,id,pembuat,pasir,batu,air): 
    folderName = input("Masukkan nama folder: ")
    folder = './save/' + folderName

    path_1 = os.path.join(folder, "user.csv")
    path_2 = os.path.join(folder, "candi.csv")
    path_3 = os.path.join(folder, "bahan_bangunan.csv")

    #Jika parent folder tidak ada
    #P.S. ini akan menimbulkan paradoks, karena jika parent folder dari awal tidak ada maka program tidak dapat diakses untuk menggunakan fungsi save
    #Maka diasumsikan bahwa parent folder sudah ada dan terdapat sub folder berisikan data csv dengan kondisi default
    if not os.path.exists('save'): 
        print()
        print("Saving . . .")
        os.mkdir('save')
        write_user(path_1, user,password,role)
        write_candi(path_2,id,pembuat,pasir,batu,air)
        write_bahan(path_3, total_pasir, total_batu, total_air)

    if not os.path.exists(folder): #Jika nama folder tidak ada di parent folder
        print()
        print("Saving . . .")
        print()
        print(f'Membuat folder {folder}...')
        print()
        print(f"Berhasil menyimpan data di folder {folder}!")
        os.mkdir(folder)
        write_user(path_1, user,password,role)
        write_candi(path_2,id,pembuat,pasir,batu,air)
        write_bahan(path_3, total_pasir, total_batu, total_air)

    elif os.path.exists(folder):    #Menjalankan fungsi  save di folder yang dituju
        print()
        print('Saving . . .')
        print()
        print(f"Berhasil menyimpan data di folder {folder}!")
        write_user(path_1, user,password,role)
        write_candi(path_2,id,pembuat,pasir,batu,air)
        write_bahan(path_3, total_pasir, total_batu, total_air)
    