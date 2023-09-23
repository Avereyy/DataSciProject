from construct import *
import rng

#Fungsi untuk melakukan batchbangun beberapa candi berdasarkan jumlah jin pembangun yang dimiliki

#KAMUS LOKAL
#list_user, list_pasir, list_batu, list_air = list
#jumlah_pasir, jumlah_batu, jumlah_air = int
#count, countnone = int
#check, checknone = bool
#temp_pasir, temp_batu, temp_air = int

#Algoritma
def batchbangun(user, role, id, pembuat, pasir, batu, air, total_pasir, total_batu, total_air):
    list_user = [' '] #Array kosong untuk list jin pembangun

    for j in range(length(role)):
        if role[j] == "jin_pembangun":
            list_user =  xappend(list_user, [user[j]]) #Mengisi array list_user dengan user role jin pembangun
    
    if list_user != [' ']: #Jika terdapat user denngan role jin pembangun, maka prosedur dibawah akan dijalankan
        jumlah_pasir = 0 ; jumlah_batu = 0 ; jumlah_air = 0 #Variabel jumlah bahan bangunan yang dimiliki
        list_pasir = [" "] ; list_batu = [" "]; list_air = [" "] #Array kosong sementara untuk jumlah bahan bangunan yang digunakan per jin
        for j in range(length(list_user)):
            temp = rng.RNGnoZERO(3) #Mengisi array bahan bangunan kosong dengan fungsi random buatan
            jumlah_pasir += temp[0]
            list_pasir = xappend(list_pasir, [temp[0]])
            jumlah_batu += temp[1]
            list_batu = xappend(list_batu, [temp[1]])
            jumlah_air += temp[2]
            list_air = xappend(list_air, [temp[2]])

        if (jumlah_pasir <= total_pasir) and (jumlah_batu <= total_batu) and (jumlah_air <= total_air): #Jika ketiga bahan bangunan mencukupi, maka prosedur dibawah akan dijalankan
            total_pasir -= jumlah_pasir #Menghitung ulang jumlah bahan bangunan yang digunakan
            total_batu -= jumlah_batu
            total_air -= jumlah_air

            count = 0 ; check = False ; checknone = False
            if pembuat[0] == 'none' and pasir[0] == 0 and batu[0] == 0 and air[0] == 0: #Jika candi pertama kosong (hancur), maka candi pertama akan diisi terlebih dahulu
                id[0] = 0
                pembuat[0] = list_user[0]
                pasir[0] = list_pasir[0]
                batu[0] = list_batu[0]
                air[0] = list_air[0]
                count += 1 ; check = True #Check akan True jika data candi pertama kosong

            if pembuat[0] != 'none' and pasir[0] != 0 and batu[0] != 0 and air[0] != 0: #Jika candi pertama ada, maka akan diperiksa jika ada candi yang hancur atau tidak di tengah" data
                countnone = 0 #Jumlah candi yang kosong (hancur)
                for l in range(1, length(id)):
                        if pembuat[l] == 'none' and pasir[l] == 0 and batu[l] == 0 and air[l] == 0: #Periksa data candi ke l yang kosong
                            countnone += 1

                        if check == False: #Jika data candi pertama ada dan tidak ada candi yang hancur, maka program akan mengisi data candi sesuai urutan
                            if countnone <= length(list_user):
                                if pembuat[l] == 'none' and pasir[l] == 0 and batu[l] == 0 and air[l] == 0 :
                                    if length(id) < 100:
                                        id[l] = id[l-1] + 1
                                        pembuat[l] = list_user[count]
                                        pasir[l] = list_pasir[count]
                                        batu[l] = list_batu[count]
                                        air[l] = list_air[count]
                                        count += 1
                                        checknone = True #Checknone akan True jika ada data candi yang kosong

                                    elif length(id) == 100: #Jika panjang candi sudah 100, maka program akan mengembalikan data bahan bangunan saja
                                        print(f"Mengerahkan {length(list_user)} jin untuk membangun candi dengan total bahan {jumlah_pasir} pasir, {jumlah_batu} batu, dan {jumlah_air} air.")
                                        return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air

                        elif check == True: #Sama seperti di atas, namun jika data candi pertama kosong, maka program akan mengisi dari data candi pertama dahulu
                            if countnone < length(list_user):
                                if pembuat[l] == 'none' and pasir[l] == 0 and batu[l] == 0 and air[l] == 0:
                                    if length(id) < 100:
                                        id[l] = id[l-1] + 1
                                        pembuat[l] = list_user[count]
                                        pasir[l] = list_pasir[count]
                                        batu[l] = list_batu[count]
                                        air[l] = list_air[count]
                                        count += 1
                                        checknone = True #Periksa jika ada candi yang hancur atau tidak
                                    else:
                                        print(f"Mengerahkan {length(list_user)} jin untuk membangun candi dengan total bahan {jumlah_pasir} pasir, {jumlah_batu} batu, dan {jumlah_air} air.")
                                        return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air

                if count < length(list_user): #Prosedur dibawah akan menjalakan prosedur jika terdapat candi yang hancur
                    if check == True: 
                        if checknone == True: #Jika terdapat candi yang hancur dan candi pertama sudah terisi, maka akan diisi candi yang hancur
                            if length(id) < 100:
                                for i in range(length(list_user)-count):
                                    id = xappend(id, [last(id) + 1])
                                    pembuat = xappend(pembuat, [list_user[count]])
                                    pasir = xappend(pasir, [list_pasir[count]])
                                    batu = xappend(batu, [list_batu[count]])
                                    air = xappend(air, [list_air[count]])
                                    count += 1
                                    if length(id) == 100:  #Pembatas jika jumlah candi sudah 100
                                        print(f"Mengerahkan {length(list_user)} jin untuk membangun candi dengan total bahan {jumlah_pasir} pasir, {jumlah_batu} batu, dan {jumlah_air} air.")
                                        return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air

                            else:
                                print(f"Mengerahkan {length(list_user)} jin untuk membangun candi dengan total bahan {jumlah_pasir} pasir, {jumlah_batu} batu, dan {jumlah_air} air.")
                                return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air
                            
                        elif checknone == False: #Jika tidak ada candi yang hancur, maka akan diisi data candi yang hancur
                            if length(id) < 100:
                                for i in range(length(list_user)-1):
                                    id = xappend(id, [last(id) + 1])
                                    pembuat = xappend(pembuat, [list_user[count]])
                                    pasir = xappend(pasir, [list_pasir[count]])
                                    batu = xappend(batu, [list_batu[count]])
                                    air = xappend(air, [list_air[count]])
                                    count += 1
                                    if length(id) == 100: #Pembatas jika jumlah candi sudah 100
                                        print(f"Mengerahkan {length(list_user)} jin untuk membangun candi dengan total bahan {jumlah_pasir} pasir, {jumlah_batu} batu, dan {jumlah_air} air.")
                                        return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air

                            else:
                                print(f"Mengerahkan {length(list_user)} jin untuk membangun candi dengan total bahan {jumlah_pasir} pasir, {jumlah_batu} batu, dan {jumlah_air} air.")
                                return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air

                    elif check == False: #Jika candi pertama sudah terisi dan ada candi yang hancur
                        if checknone == True:
                            if length(id) < 100: #Prosedur mengisi data candi dimulai dari ID == 1 dan candi yang hancur akan diisi
                                    id = xappend(id, [last(id) + 1])
                                    pembuat = xappend(pembuat, [list_user[count]])
                                    pasir = xappend(pasir, [list_pasir[count]])
                                    batu = xappend(batu, [list_batu[count]])
                                    air = xappend(air, [list_air[count]])
                                    count += 1
                                    if length(id) == 100: #Pembatas jika jumlah candi sudah 100
                                        print(f"Mengerahkan {length(list_user)} jin untuk membangun candi dengan total bahan {jumlah_pasir} pasir, {jumlah_batu} batu, dan {jumlah_air} air.")
                                        return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air
                            else:
                                print(f"Mengerahkan {length(list_user)} jin untuk membangun candi dengan total bahan {jumlah_pasir} pasir, {jumlah_batu} batu, dan {jumlah_air} air.")
                                return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air

                        elif checknone == False: #Jika tidak ada candi yang hancur, maka prosedur dibawah akan dijalankan
                            if length(id) < 100 :
                                #Prosedur akan mengisi data dari awal sampai array list_user dan array bahan terisi di array candi
                                for i in range(length(list_user)):
                                    id = xappend(id, [last(id) + 1])
                                    pembuat = xappend(pembuat, [list_user[count]])
                                    pasir = xappend(pasir, [list_pasir[count]])
                                    batu = xappend(batu, [list_batu[count]])
                                    air = xappend(air, [list_air[count]])
                                    count += 1
                                    if length(id) == 100: #Pembatas jika jumlah candi sudah 100
                                        print(f"Mengerahkan {length(list_user)} jin untuk membangun candi dengan total bahan {jumlah_pasir} pasir, {jumlah_batu} batu, dan {jumlah_air} air.")
                                        return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air
                                    
                                    
                            else: #Jika jumlah candi sudah 100 maka akan mengembalikan bahan bangunan saja
                                print(f"Mengerahkan {length(list_user)} jin untuk membangun candi dengan total bahan {jumlah_pasir} pasir, {jumlah_batu} batu, dan {jumlah_air} air.")
                                return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air

            print(f"Mengerahkan {length(list_user)} jin untuk membangun candi dengan total bahan {jumlah_pasir} pasir, {jumlah_batu} batu, dan {jumlah_air} air.")
            return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air


        else: #Jika ada satu atau lebih bahan bangunan yang tidak mencukupi untuk batch bangun
            temp_pasir = total_pasir - jumlah_pasir
            temp_batu = total_pasir - jumlah_batu
            temp_air = total_air - jumlah_air

            #Periksa apakah bahan cukup atau kurang dan ubah outputnya
            if temp_pasir >= 0 :
                temp_pasir = 0
            else:
                temp_pasir = -temp_pasir

            if temp_batu >= 0 :
                temp_batu = 0
            else:
                temp_batu = -temp_batu

            if temp_air >= 0:
                temp_air = 0
            else:
                temp_air = -temp_air
            print(f"Bangun gagal. Kurang {temp_pasir} pasir, {temp_batu} batu, dan {temp_air} air.")
            return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air 

    #Jika tidak ada jin pengumpul, maka batchbangun akan gagal
    else:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
        return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air

