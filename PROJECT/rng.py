import time
from construct import *
#Fungsi untuk mencari integer acak

#KAMUS LOKAL
#current_time = integer
#random_integers = list

#Algoritma
def RNG(): #Fungsi random number generator menggunakan linear congruential generator (LCG) dengan module time
    #Xn+1 = (a.Xn + c) mod m
    current_time = int(round(time.time() * 1000))
    return ((current_time * 1103515245 + 12345) % 2**31) / (2**31 - 1)

def RNGs(n): #Memanggil fungsi random yang diulang ke n kali
    random_integers = [0 for i in range(n)]
    for i in range(n):
        time.sleep(0.01)
        random_integers[i] = int(RNG() * 6)
    return random_integers

def RNGnoZERO(n): #Fungsi untuk menghasilkan array tanpa nilai 0
    random_integers = [0 for i in range(n)]
    for i in range(n):
        time.sleep(0.00001)
        random_integers[i] = int(RNG() * 5) + 1
    return random_integers
