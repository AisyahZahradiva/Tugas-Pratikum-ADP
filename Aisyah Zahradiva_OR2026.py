#Soal 14
#Fungsi untuk mengecek bilangan prima atau tidak
def prima(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

#Fungsi untuk melakukan transformasi
def transformasi(x):
    s= str(x)
    n= len(s)
    hasil=[]
    for i in range(n):
        for j in "0123456789":
            if s[i] == j:
                continue
            s_ganti= s[:i] + j + s[i+1:]
            if s_ganti[0] == "0":
                continue
            s_baru=int(s_ganti)
            if prima(s_baru) == True:
                hasil.append(s_baru)
                break
    return hasil
            
#Program utama
while True:
    print("Masukkan bilangan bulat positif")
    x=int(input("> "))
    if x <= 0:
        print(f"Maaf {x} bukan bilangan bulat positif")
    else:
        break
Hasil= transformasi(x)
if Hasil == []:
    print(f"Bilangan {x} tidak memiliki transformasi yang menghasilkan bilangan prima, sehingga {x} bukan merupakan Prime Transformation Number.")
else:
    print(f"Bilangan {x} merupakan Prime Transformation Number, dengan bilangan prima hasil transformasi yaitu", end=" ")
    for u in range(len(Hasil)): 
        if u == len(Hasil)-1:
            print(Hasil[u], ".")
        else:
            print(Hasil[u], end=", ")
