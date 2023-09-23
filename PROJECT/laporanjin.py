from construct import *

#Prosedur untuk menampilkan informasi terkait jin yang ada di data permainan

#KAMUS LOKAL
#jumlah_pengumpul, jumlah_pembangun, total, total_candi = integer
#list_jumlah, list_pembangun, matriks_pembangun = list
#cek, count = integer
#n ,m jin_terajin, jin_termalas = string

#Algoritma
def laporan(user, role, pembuat, total_pasir, total_batu, total_air,id,pasir,batu,air):
    jumlah_pengumpul = 0
    jumlah_pembangun = 0
    total = 0 ; total_candi = 0
    for i in range(length(role)): #Menghitung jumlah jin berdasarkan kategori dan jumlah candi yang valid
        if role[i] == "jin_pengumpul":
            jumlah_pengumpul += 1
            total += 1
        elif role[i] == 'jin_pembangun':
            jumlah_pembangun += 1
            total += 1
    for i in range(length(pembuat)):
        if pembuat[i] != 'none' and id[i] != 0 and pasir[i] != 0 and batu[i] != 0 and air[i] != 0:
            total_candi += 1

    list_pembangun = [" "] #Array berisikan semua jin pembangun
    for i in range(length(user)):
        if role[i] == "jin_pembangun":
            list_pembangun = xappend(list_pembangun, [user[i]])

    list_jumlah = [0 for i in range(length(list_pembangun))] #Menghitung jumlah candi yang dibangun per jin pembangun
    for i in range(length(list_jumlah)):
        for j in range(length(pembuat)):
            if list_pembangun[i] == pembuat[j]:
                list_jumlah[i] += 1

    matriks_pembangun = [[" " for i in range(2)] for i in range(length(list_jumlah))] #Matriks nama jin dan jumlah candi yang dibangun
    for i in range(length(list_jumlah)):
        matriks_pembangun[i][0] = list_pembangun[i]
        matriks_pembangun[i][1] = list_jumlah[i]


    for i in range(length(list_jumlah)-1): #Mengurutkan matriks dari candi paling banyak yang dibuat
        for j in range(length(list_jumlah)-1):
            if matriks_pembangun[j][1] < matriks_pembangun[j+1][1]:
                matriks_pembangun[j], matriks_pembangun[j+1] = matriks_pembangun[j+1], matriks_pembangun[j]    
    
    if total_candi == 0: #Jika jumlah candi 0
        jin_terajin = "-"
        jin_termalas = "-"
        return print(), print(f"> Total Jin: {total}"), print(f"> Total Jin Pengumpul: {jumlah_pengumpul}"), print(f"> Total Jin Pembangun: {jumlah_pembangun}"), print(f"> Jin Terajin: {jin_terajin}"), print(f"> Jin Termalas: {jin_termalas}") , print(f"> Jumlah Pasir: {total_pasir} unit"), print(f"> Jumlah Air: {total_air} unit"), print(f"> Jumlah Batu: {total_batu} unit")

    #OProsedur dibawah menentukan jin paling rajin dan paling malas
    jin_terajin = matriks_pembangun[0][0]
    for i in range(length(list_jumlah)):
        jin_termalas = matriks_pembangun[i][0]

    if length(list_jumlah) > 2:
        list_rajin = [" "] ; list_malas = [" "] #Array dari jumlah candi terbanyak dan terdikit yang sama
        n = matriks_pembangun[0][1]
        for i in range(length(list_jumlah)):
            m = matriks_pembangun[i][1]

        for i in range(length(list_jumlah)): #Memilah jin berdasarkan jumlah candi yang terbanyak dan sedikit
            if matriks_pembangun[i][1] == n:
                list_rajin = xappend(list_rajin, [matriks_pembangun[i][0]])
            elif matriks_pembangun[i][1] == m:
                list_malas = xappend(list_malas, [matriks_pembangun[i][0]])
                
        list_rajin = namesort(list_rajin) #Menyusun nama jin secara leksikografis
        jin_terajin = list_rajin[0]
        list_malas = namesort(list_malas)
        jin_termalas = list_malas[0]

    cek = list_jumlah[0] ; count = 0 
    for i in range(length(list_jumlah)): #Jika kondisi jumlah candi yang dibangun sama rata
        if list_jumlah[i] == cek:
            count += 1
            
    if count == length(list_jumlah): #Akan memilih secara urutan pertama dan kedua
        list_pembangun = namesort(list_pembangun)
        jin_terajin = list_pembangun[0]
        if length(list_jumlah) > 1:
            jin_termalas = list_pembangun[1]
    
    #Mencetak output
    print()
    print(f"> Total Jin: {total}")
    print(f"> Total Jin Pengumpul: {jumlah_pengumpul}")
    print(f"> Total Jin Pembangun: {jumlah_pembangun}")
    print(f"> Jin Terajin: {jin_terajin}")
    print(f"> Jin Termalas: {jin_termalas}")
    print(f"> Jumlah Pasir: {total_pasir} unit")
    print(f"> Jumlah Air: {total_air} unit")
    print(f"> Jumlah Batu: {total_batu} unit")

        
