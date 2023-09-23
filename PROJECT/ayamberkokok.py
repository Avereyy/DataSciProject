from construct import *

#Fungsi ayam berkokok untuk menentukan pemenang permainan

#KAMUS LOKAL
#candi = integer

#Algoritma
def ayamberkokok(pembuat, pasir, batu, air):
    candi = 0
    for i in range(length(pembuat)):
        if pembuat[i] != 'none' and pasir[i] != 0  and batu[i] != 0 and air[i] != 0: 
            candi += 1 #menghitung jumlah candi yang valid
    
    if candi < 100: #jika candi bernilai kurang dari 100, Roro memenangnkan permainan
        print("Kukuruyuk.. Kukuruyuk..")
        print()
        print(f"Jumlah Candi: {candi}")
        print()
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print()
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
        return False #Nilai False akan memberhentikan loop dan akan langsung keluar program
    
    elif candi == 100: #Jika jumlah candi sama dengan 100, maka Bondowoso akan menang
        print("Kukuruyuk.. Kukuruyuk..")
        print()
        print(f"Jumlah Candi: {candi}")
        print()
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        return False
    
