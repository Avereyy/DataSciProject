from construct import *

#Prosedur untuk menampilkan informasi terkait candi yang ada di data permainan

#KAMUS LOKAL
#jumlah_candi, jumlah_pasir, jumlah_batu, jumlah_air = integer
#list_id, list_harga, matriks_harga = list
#id_termahal, id_termurah = integer
#harga_termhala, harga_termurah = string

#Algoritma
def laporancandi(id, pembuat, pasir, batu, air):
    jumlah_candi = 0 ; jumlah_pasir = 0 ; jumlah_batu = 0 ; jumlah_air = 0
    for i in range(length(id)):
        if pembuat[i] != 'none' and pasir[i] != 0 and batu[i] != 0 and air[i] != 0: #Cek jumlah candi yang tidak hancur
            jumlah_candi += 1
            
    if jumlah_candi > 0: #Jika ada candi maka prosedur dibawah akan dijalankan
        for i in range(length(pasir)): #Menghitung jumlah total bahan bangunan
            jumlah_pasir += pasir[i]

        for i in range(length(batu)):
            jumlah_batu += batu[i]

        for i in range(length(air)):
            jumlah_air += air[i]

        list_id = [" "] #Array id yang berisikan data candi tidak hancur
        for i in range(length(id)):
            if pembuat[i] != 'none':
                list_id = xappend(list_id, [id[i]])

        list_harga = [" "] #Array harga dari candi  yang valid
        for i in range(length(id)):
            if pembuat[i] != 'none':
                harga = pasir[i] * 10000 + batu[i] * 15000 + air[i] * 7500
                list_harga = xappend(list_harga, [harga])

        matriks_harga = [[" " for i in range(2)] for i in range(jumlah_candi)] #Matriks harga candi dengan ID dan harga candi
        for i in range(jumlah_candi):
            matriks_harga[i][0] = list_id[i]
            matriks_harga[i][1] = list_harga[i]

        for i in range(jumlah_candi-1): #Mengurutkan harga candi dari paling mahal ke paling murah
            for j in range(jumlah_candi-1):
                if matriks_harga[j][1] < matriks_harga[j+1][1]:
                    matriks_harga[j], matriks_harga[j+1] = matriks_harga[j+1], matriks_harga[j]

        id_termahal = matriks_harga[0][0] #Mengambil data termahal dan termurah
        harga_termahal = matriks_harga[0][1]

        for j in range(jumlah_candi):
            id_termurah = matriks_harga[j][0]
            harga_termurah = matriks_harga[j][1]

        harga_termahal = rupiah(harga_termahal) #konversi menjadi nilai rupiah
        harga_termurah = rupiah(harga_termurah)

        print()
        print(f"> Total Candi: {jumlah_candi}")
        print(f"> Total Pasir yang digunakan: {jumlah_pasir}")
        print(f"> Total Batu yang digunakan: {jumlah_batu}")
        print(f"> Total Air yang digunakan: {jumlah_air}")
        print(f"ID Candi Termahal: {id_termahal} (Rp {harga_termahal})")
        print(f"ID Candi Termurah: {id_termurah} (Rp {harga_termurah})")

    elif jumlah_candi == 0: #Jika jumlah candi 0, maka output akan seperti dibawah
        print()
        print(f"> Total Candi: {jumlah_candi}")
        print(f"> Total Pasir yang digunakan: 0 ")
        print(f"> Total Batu yang digunakan: 0")
        print(f"> Total Air yang digunakan: 0")
        print(f"ID Candi Termahal: -")
        print(f"ID Candi Termurah: -")
