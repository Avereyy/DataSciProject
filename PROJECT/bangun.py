from construct import *
import rng

#Fungsi untuk membangun candi oleh pengguna jin

#KAMUS LOKAL
#max, countnone, count0 = integer
#temp = list
#temp_pasir, temp_air. temp_batu = integer
#newest_id, new_pembuat, new_pasir_2, new_batu_2, new_air_2 = list

#Algoritma
def bangun(id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air ,username):

    max = 100 ; countnone = 0
    for i in range(length(id)):
        if pembuat[i] != 'none' and pasir[i] != 0 and batu[i] != 0 and air[i] != 0:
            countnone += 1 #Menghitung jumlah candi yang valid di awal

    if countnone < 100: #Kondisi pertama, jika jumlah candi valid kurang dari 100

        if pembuat[0] == 'none' and pasir[0] == 0 and batu[0] == 0 and air[0] == 0: #Periksa jika candi pertama (ID == 0) yang kosong
            pembuat[0] = username
            temp = rng.RNGnoZERO(3) #Memanggil nilai bahan dengan fungsi random buatan
            new_pasir = temp[0]
            new_batu = temp[1]
            new_air = temp[2]

            if new_pasir <= total_pasir and new_batu < total_batu and new_air < total_air:
                total_pasir -= new_pasir #Menghitung jumlah bahan bangunan baru
                total_batu -= new_batu
                total_air -= new_air
                pasir[0] = new_pasir ; batu[0] = new_batu ; air[0] = new_air #Jika bahan cukup, maka candi dengan ID == 0 akan terisi duluan
                print("Candi berhasil dibangun.")
                print(f"Sisa candi yang perlu dibangun: {max - 1}.")
                return id, pembuat, pasir, batu, air, total_pasir, total_batu, total_air
            
            else:
                print("Bahan bangunan tidak mencukupi.")
                print("Candi tidak bisa dibangun!")
                return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air
                
            

        elif pembuat[0] != 'none': #Jika candi pertama ada isi, maka program akan memeriksa candi sesudahnya
                for i in range(1, length(id)):
                    if (pembuat[i] == 'none'and pasir[i] == 0 and batu[i] == 0 and air[i] == 0): #Periksa jika ada data candi yang kosong (dihancurkan)
                        newest_id = [" "] ; new_pembuat = [" "] ; new_pasir_2 = [" "] ; new_batu_2 = [" "] ; new_air_2 = [" "] #Array kosong sementara untuk diisi nantinya
                        max = 99 #Max bernilai 99 karena candi pertama sudah dibangun

                        temp = rng.RNGnoZERO(3)
                        temp_pasir = temp[0]
                        temp_batu = temp[1]
                        temp_air = temp[2]

                        if temp_pasir <= total_pasir and temp_batu < total_batu and temp_air < total_air: #Jika bahan bangunan cukup, maka program akan menjalankan prosesur dibawah
                            total_pasir -= temp_pasir #Menghitung jumlah bahan bangunan baru
                            total_batu -= temp_batu
                            total_air -= temp_air

                            for j in range(0,i): #Menaruh data dari awal sampai data yang kosong
                                newest_id = xappend(newest_id, [id[j]])
                                new_pembuat = xappend(new_pembuat, [pembuat[j]])
                                new_pasir_2 = xappend(new_pasir_2, [pasir[j]])
                                new_batu_2 = xappend(new_batu_2, [batu[j]])
                                new_air_2 = xappend(new_air_2, [air[j]])

                            newest_id = xappend(newest_id, [newest_id[j]+1])  #Mengisi data yang kosong
                            new_pembuat = xappend(new_pembuat, [username])
                            new_pasir_2 = xappend(new_pasir_2, [temp_pasir])
                            new_batu_2 = xappend(new_batu_2, [temp_batu])
                            new_air_2 = xappend(new_air_2, [temp_air])

                            for k in range(i+1, length(pembuat)): #Mengisi data dari yang kosong sampai data terakhir
                                newest_id = xappend(newest_id, [id[k]])
                                new_pembuat = xappend(new_pembuat, [pembuat[k]])
                                new_pasir_2 = xappend(new_pasir_2, [pasir[k]])
                                new_batu_2 = xappend(new_batu_2, [batu[k]])
                                new_air_2 = xappend(new_air_2, [air[k]])
                            print()
                            print("Candi berhasil dibangun.")
                            count = 0
                            for l in range(1,length(id)):
                                if id[l] != 0:
                                    count += 1
                            count += 1
                            print(f"Sisa candi yang perlu dibangun: {max - count}.")
                            return newest_id, new_pembuat, new_pasir_2, new_batu_2, new_air_2, total_pasir, total_batu, total_air
                            
                        else: #Jika bahan tidak cukup, maka tidak mengembalikan apa"
                            print()
                            print("Bahan bangunan tidak mencukupi.")
                            print("Candi tidak bisa dibangun!")
                            return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air
                
                max = 99
                temp = rng.RNGnoZERO(3)
                temp_pasir = temp[0]
                temp_batu = temp[1]
                temp_air = temp[2]

                if temp_pasir <= total_pasir and temp_batu < total_batu and temp_air < total_air: 
                    total_pasir -= temp_pasir #Menghitung jumlah bahan yang berkurang karena bangun
                    total_batu -= temp_batu
                    total_air -= temp_air
                    #Jika tidak ada candi yang hancur, maka prosedur dibawah akan dijalankan
                    for i in range(length(id)):
                        newest_id = xappend(id, [id[i] + 1])
                    for i in range(length(id)): #Mengisi data candi terakhir dengan data candi baru
                        new_pembuat = xappend(pembuat, [username])
                        new_pasir_2 = xappend(pasir, [temp_pasir])
                        new_batu_2 = xappend(batu, [temp_batu])
                        new_air_2 = xappend(air, [temp_air])
                        print()
                        print("Candi berhasil dibangun.")
                        print(f"Sisa candi yang perlu dibangun: {max - length(id)}.")
                        return newest_id, new_pembuat, new_pasir_2, new_batu_2, new_air_2,total_pasir, total_batu, total_air
                else:
                    print()
                    print("Bahan bangunan tidak mencukupi.")
                    print("Candi tidak bisa dibangun!")
                    return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air

    elif countnone >= 100: #Jika jumlah candi sudah memenuhi 100, maka nilai dari pasir, batu, dan air akan berkurang namun tidak ada perubahan
        temp = rng.RNGnoZERO(3) #pada data candi
        temp_pasir = temp[0]
        temp_batu = temp[1]
        temp_air = temp[2]

        if temp_pasir <= total_pasir and temp_batu < total_batu and temp_air < total_air:
            total_pasir -= temp_pasir
            total_batu -= temp_batu
            total_air -= temp_air
            print() #Jika bahan cukup, bahan berubah
            print("Candi berhasil dibangun.")
            return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air

        else:
            print() #Jika bahan tidak cukup, tidak mengembalikan apa"
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
            return id, pembuat, pasir, batu, air,total_pasir, total_batu, total_air