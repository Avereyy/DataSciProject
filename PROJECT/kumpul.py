import rng

#Prosedur untuk mengumpulkan bahan bangunan oleh jin pengumpul

#KAMUS LOKAL
#temp = list

#Algoritma
def kumpul(pasir, batu, air):
    temp = rng.RNGs(3) #Array berisikan 3 angka acak (0-5) untuk dijadikan bahan
    pasir += temp[0]
    batu += temp[1]
    air += temp[2]
    print(f"Jin mengumpulkan {temp[0]} pasir, {temp[1]} batu, dan {temp[2]} air")
    return pasir, batu, air
