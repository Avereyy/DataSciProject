from construct import *

#Prosedur untuk menghancurkan candi

#KAMUS LOKAL
#check = bool
#id, pembuat, pasir, batu, air = list
#count, id_candi = integer
#ans = string

#Algoritma
def hancur(list_id, list_pembuat, list_pasir, list_batu, list_air):
    check = True
    if list_pembuat[0] == 'none' and list_pasir[0] == 0 and list_batu[0] == 0 and list_air[0] == 0 and length(list_id) == 1:
        check = False #Periksa hanya ada satu candi dalam data candi

    while check == True: #Jika terdapat candi, maka prosedur dibawah akan dijalankan
        id = [" "] ; pembuat = [" "] ; pasir = [" "] ; batu = [" "] ; air = [" "] #Arry baru yang akan diisi data candi abru
        count = 0
        id_candi = int(input("Masukkan ID candi: "))
        for i in range(length(list_id)):
            if id_candi == list_id[i]: #cek candi ada atau tidak
                ans = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)? ")
                if ans == "Y":
                    for i in range(length(list_id)):
                        if id_candi == i: #Jika candi ingin dihancurkan, maka candi tsb akan diganti data nya ke 0;none;0;0;0
                            id = xappend(id, [0])
                            pembuat = xappend(pembuat, ['none'])
                            pasir = xappend(pasir,[0])
                            batu = xappend(batu, [0])
                            air = xappend(air, [0])
                        elif id_candi != i: #Mengisi sisa candi yang tidak dihancurkan
                            id = xappend(id, [list_id[i]])
                            pembuat = xappend(pembuat, [str(list_pembuat[i])])
                            pasir = xappend(pasir, [list_pasir[i]])
                            batu = xappend(batu, [list_batu[i]])
                            air = xappend(air, [list_air[i]])
                    print()
                    print("Candi telah berhasil dihancurkan.")
                    return id, pembuat,pasir,batu,air
                else:
                    print()
                    print("Candi telah gagal dihancurkan.")
                    return list_id, list_pembuat, list_pasir, list_batu, list_air
            else:
                count += 1

            if count == length(list_id): #Jika tidak ada candi dengan ID yang diinput
                print()
                print("Tidak ada candi dengan ID tersebut.")
                return list_id, list_pembuat, list_pasir, list_batu, list_air
            
   
    print()
    print("Tidak ada candi yang telah dibuat.")
    return list_id, list_pembuat, list_pasir, list_batu, list_air
