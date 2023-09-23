from construct import *
import rng

#Fungsi untuk melakukan batchbangun bahan bangunan berdasarkan jumlah jin pengumpul yang dimiliki

#KAMUS LOKAL
#temp = list
#pasir, batu, air = integer
#n = integer

#Algoritma
def kumpul():
    temp = rng.RNGs(3) #Memanggil array dengan 3 nilai random
    return temp

def batchkumpul(role, total_pasir, total_batu, total_air):
    n = 0
    pasir = 0 ; batu = 0 ; air = 0
    for i in range(length(role)): #Menghitung jumlah jin pengumpul yang ada
        if role[i] == "jin_pengumpul":
            n += 1

    if n != 0:
        for i in range(n): #Menambah jumlah bahan bangunan berdasarkan jumlah jin pengumpul yang ada
            pasir += (kumpul()[0])
            batu += (kumpul()[1])
            air += (kumpul()[2])
            
        #Mengubah nilai total dengan memambahkan hasil batch kumpul
        total_pasir += pasir
        total_batu += batu
        total_air += air

        print(f"Mengerahkan {n} jin untuk mengumpulkan bahan.")
        print(f"Jin menemukan total {pasir} pasir, {batu} batu, dan {air} air.")
        return total_pasir , total_batu , total_air #Mencetak hasil dan mengembalikan jumlah bahan bangunan

    #Jika tidak ada jin pengumpul, maka tidak mengubah nilai bahan bangunan
    elif n == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
        return total_pasir ,total_batu , total_air
