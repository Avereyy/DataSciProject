#Berikut merupakan beberapa fungsi buatan untuk memudahkan proses prosedur untuk menjalankan program
#sesuai ketentuan yang ada

#KAMUS LOKAL
#length -> var = string ; count = integer
#dumstring -> dumstr = string ; index = integer
#xappend -> k, n, l = integer ; temp = list
#newlist -> elmt, final = list
#cekstr -> newstr = list
#write_user -> var, arr_user = string
#checkKosong -> new_id, new_pembuat, new_pasir, new_batu, new_air = list ; num = integer
#write_bahan -> temp, var, arr_bahan, str_bahan = string
#write_candi -> temp, var, arr_candi = string
#rupiah -> angka, dum, dum2, final = string
#namesort -> n = integer
#users -> user, password, role = list ; char = string ; k, parameter = integer
#bahan -> nama, deskripsi, jumlah = list ; char = string ; k, parameter = integer
#candi -> id, pembuat, pasir, batu, air = list ; char = string ; k, parameter = integer

#Algoritma
def length(item): #Menghitung panjang dari suatu string maupun array list
    if type(item) == str:
        return len(item)
    else:
        var = str(item) ; count = 0
        for i in range(len(var)):
            if var[i] == ',':
                count += 1
    count += 1
    return count

def dumstring(list): #mengubah list[i] menjadi str
    if length(list) == 0:
        return ""
    dumstr = str(list[0])
    index = 1
    while index < length(list):
        dumstr += "" + str(list[index])
        index += 1

    return dumstr

def last(list): #Mengembalikan elemen terakhir di list
    for i in range(length(list)):
        last = i
    return last

def xappend(list,var): #Membuat list kosong dengan panjang tertentu dan menambahkan elemen yang diinginkan kedalam list tersebut
    k = length(var) 
    n = length(list)
    if list == [" "]:
        n = 0
    temp = ["&" for i in range(n+k)] 
    for i in range(length(temp)-k):
        temp[i] = list[i]
    l = 0
    for j in range(length(temp)-k,length(temp),1):
        temp[j] = var[l]
        l += 1
    return temp

def newlist(lst): #untuk menghasilkan list tanpa karakter "&"
    elmt = xappend(lst, "&")
    final = [" "]
    for i in range(length(elmt)):
        if elmt[i] == "&":
            break
        elif elmt[i] != " " and (i != 0):
            final = xappend(final, [elmt[i]])

    return final 

def STRtoINT(list): #Mengubah nilai dalam list yang awalnya berupa string menjadi integer
    for i in range(length(list)):
        list[i] = int(list[i])
    return list

def cekstr(dumstring): #cek jika elemen str ada karakter "\n" dan mengembalikan elemen tanpa karakter "\n"
    newstr = ["&" for i in range(length(dumstring))]
    for i in range(length(dumstring)):
        for j in range(length(dumstring[i])):
            if dumstring[i][j] == "\n":
                break
            else:
                if newstr[i] == "&":
                    newstr[i] = str(dumstring[i][j])
                else:
                    newstr[i] += str(dumstring[i][j])
    return newstr

def write_user(path, user, password, role): #Me-write list data user kedalam csv
    var = ""
    for i in range(length(user)):
        if i < length(user):
            var += user[i] + ";" + password[i] + ";" + role[i] + '\n' #newline jika line belum paling bawah
        else:
            var += user[i] + ";" + password[i] + ";" + role[i]
    arr_user = "username;password;role" + '\n' + var
    with open(path, 'w') as f:
        f.write(arr_user)
    
def checkKosong(id, pembuat, pasir, batu, air): #Periksa jika data list candi terdapat elemen kosong dan mengisi list tersebut dengan elemen awal
    new_id = [" "] ;  new_pembuat = [" "] ; new_pasir = [" "] ; new_batu = [" "] ; new_air = [" "]
    num = 0 
    for i in range(length(id)):
        while num < id[i]:
            new_id = xappend(new_id, [0])
            new_pembuat = xappend(new_pembuat, ['none'])
            new_pasir =  xappend(new_pasir, [0])
            new_batu = xappend(new_batu, [0])
            new_air = xappend(new_air, [0])
            num += 1

        new_id = xappend(new_id, [id[i]])
        new_pembuat = xappend(new_pembuat, [pembuat[i]])
        new_pasir =  xappend(new_pasir, [pasir[i]])
        new_batu = xappend(new_batu, [batu[i]])
        new_air = xappend(new_air, [air[i]])
        num += 1
    return new_id, new_pembuat, new_pasir, new_batu, new_air

def write_bahan(path, pasir, batu, air): #Me-write list data bahan bangunan kedalam csv
    temp = "nama;deskripsi;jumlah" + '\n'
    var = ''
    arr_bahan = temp
    if pasir != 0 and batu != 0 and air != 0: #Jika bahan bangunan ada isi, maka akan menuliskan data dibawah
        pasir = "pasir;dari pantai;" + str(pasir) + '\n'
        batu = "batu;dari gunung;" + str(batu) + '\n' 
        air =  "air;dari sungai;" + str(air)
        str_bahan = pasir + batu + air
        arr_bahan += str_bahan
    else:
        arr_bahan += var #Namun jika bahan bangunan kosong, maka menuliskan kondisi default csv bahan bangunan

    with open(path, 'w') as f:
        f.write(arr_bahan)

def write_candi(path,id,pembuat,pasir,batu,air): #Me-write list data candi kedalam csv
    temp = "id;pembuat;pasir;batu;air"
    var = ''
    for i in range(length(id)):
        if pembuat[i] != 'none':
            if i < length(id):
                var += str(id[i]) + ';' + pembuat[i] + ";"+ str(pasir[i]) + ";" + str(batu[i]) + ";" + str(air[i]) + '\n' #Membuat line baru jika belum di line paling akir
            else:
                var += str(id[i]) + ';' + pembuat[i] + ";"+ str(pasir[i]) + ";" + str(batu[i]) + ";" + str(air[i])
    arr_candi = temp + '\n' + var
    with open(path, "w") as f:
        f.write(arr_candi)

def rupiah(angka): #Merubah integer angka menjadi format string angka dengan pembagi titik ribuan
    angka = str(angka)
    dum = ""; dum2 = ""
    for i in range(length(angka)):
        if i < length(angka)-3:
            dum += angka[i]
        elif i >= length(angka)-3:
            dum2 += angka[i]
    final = dum + "." + dum2
    return final

def namesort(lst): #Mengurutkan list elemen str secara leksikografis
    n = length(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


#untuk user csv
def users(csv_1): #Mengubah tiap elemen pada user csv menjadi array tersendiri
    with open(csv_1) as file:
        rows = file.readlines()
    user = ["&" for i in range(105)]
    password = ["&" for i in range(105)]
    role = ["&" for i in range(105)]
    char = ""
    k = 0
    parameter = 0

    for i in range(length(rows)): 
        dumarray = rows[i]
        dumstr = dumstring(dumarray)
        for j in range(length(dumstr)): #Memisahkan elemen dengan pembagi karakter ";"
            if dumstr[j] == ";":
                parameter += 1
                if parameter == 1:
                    user[k] = char
                    char = ""
                elif parameter == 2:
                    password[k] = char
                    char = ""
            elif j == (length(dumstr)-1):
                    role[k] = char + dumstr[length(dumstr)-1]
                    char = ""

            elif dumstr[j] != ";":
                char += dumstr[j]
        char =""
        k += 1
        parameter = 0
    return newlist(user), newlist(password), cekstr(newlist(role))

#untuk bahan bangunan
def bahan(csv_2): #Mengubah tiap elemen pada csv bahan_bangunan menjadi array tersendiri
    with open(csv_2) as file:
        bahan = file.readlines()
    nama = ["&" for i in range(105)]
    deskripsi = ["&" for i in range(105)]
    jumlah = ["&" for i in range(105)] #int

    char = ""
    k = 0
    parameter = 0

    for i in range(length(bahan)): 
        dumarray = bahan[i]
        dumstr = dumstring(dumarray)
        for j in range(length(dumstr)): #Memisahkan elemen dengan pembagi karakter ";"
            if dumstr[j] == ";":
                parameter += 1
                if parameter == 1:
                    nama[k] = char
                    char = ""
                elif parameter == 2:
                    deskripsi[k] = char
                    char = ""
            elif j == (length(dumstr)-1):
                    jumlah[k] = char + dumstr[length(dumstr)-1]
                    char = ""

            elif dumstr[j] != ";":
                char += dumstr[j]

        char =""
        k += 1
        parameter = 0
    return newlist(nama),newlist(deskripsi), STRtoINT(cekstr(newlist(jumlah)))

#untuk candi
def candi(csv_3): #Mengubah tiap elemen pada csv candi menjadi array tersendiri

    with open(csv_3) as file:
        candi = file.readlines()
    id = ["&" for i in range(105)] #int
    pembuat = ["&" for i in range(105)]
    pasir = ["&" for i in range(105)] #int
    batu = ["&" for i in range(105)] #int
    air = ["&" for i in range(105)] #int

    char = ""
    k = 0
    parameter = 0

    for i in range(length(candi)): 
        dumarray = candi[i]
        dumstr = dumstring(dumarray)
        for j in range(length(dumstr)): #Memisahkan elemen dengan pembagi karakter ";"
            if dumstr[j] == ";":
                parameter += 1
                if parameter == 1:
                    id[k] = char 
                    char = ""
                elif parameter == 2:
                    pembuat[k] = char
                    char = ""
                elif parameter == 3:
                    pasir[k] = char 
                    char = ""
                elif parameter == 4:
                    batu[k] = char 
                    char = ""

            elif j == (length(dumstr)-1):
                    air[k] = char + dumstr[length(dumstr)-1]
                    char = ""

            elif dumstr[j] != ";":
                char += dumstr[j]

        char =""
        k += 1
        parameter = 0
    return (STRtoINT(newlist(id))), (newlist(pembuat)), STRtoINT(newlist(pasir)), STRtoINT(newlist(batu)), STRtoINT(cekstr(newlist(air)))
