#Tahun 2024 No. 1
'''
while True:
    a= int(input('Masukkan a(harus positif): '))
    b= int(input('Masukkan b(harus positif): '))
    if a<0 or b<0:
        print('Silahkan masukkan angka yang positif')
        break 
    if a>b:
        print('Input tidak valid')
    elif a<=b:
        for i in range(a,b+1):
            if i==1:
                continue
            for j in range(2,i):
                if i%j == 0:
                    break 
            else:
                print(f'{i}', end=' ')
        break
'''

#Tahun 2024 No. 2
'''
utbk= int(input('UTBK = '))
teofl= int(input('TEOFL = '))
if utbk>1000 or utbk<200 or teofl>677 or teofl<310:
    print('Input tidak valid')
elif utbk<500 or teofl<400:
    print('Mahasiswa tidak diterima di UNAND')
else:
    if utbk>=700 and teofl>=500:
        print('Besar UKT 500000')
    elif utbk>=700 and (teofl>=400 or teofl<500):
        print('Besar UKT 2000000')
    elif utbk<700 and teofl>=500:
        print('Besar UKT 3500000')
    elif utbk<700 and (teofl>=400 or teofl<500):
        print('Besar UKT 5000000')
'''

#Tahun 2023 No. 1
'''
n= int(input('Jumlah data = '))
data1=[]
for i in range(n):
    a_i= int(input(f'data a_{i+1} = '))
    data1.append(a_i)
print(f'Data sebelum diurut = ', end='')
for i in range(n):
    if i==n-1:
        print(f'{data1[i]}')
    else:
        print(f'{data1[i]}', end=',')
data2= data1.copy()
batas= n
while batas>1:
    for i in range(batas-1):
        if data2[i]>data2[i+1]:
            tukar= data2[i]
            data2[i]=data2[i+1]
            data2[i+1]=tukar
    batas-=1
print(f'Data setelah diurut = ', end='')
for i in range(n):
    if i==n-1:
        print(f'{data2[i]}')
    else:
        print(f'{data2[i]}', end=',')
print(f'Data terbesar = {data2[-1]}')
print(f'Data terkecil = {data2[0]}')
'''

#Tahun 2023 No. 2
'''
def prima(n):
    ''''prime= False''''
    for i in range(2,n):
        if n%i == 0:
            prime= False
            break
        else:
            prime= True
    return prime

#main program
n= int(input('n = '))
if n>0:
    prima= prima(n)
    if prima==True:
        print(f'Bilangan {n} adalah bilangan prima')
    else:
        print(f'Bilangan {n} bukan bilangan prima')
'''

#Tahun 2023 No. 3
'''
def kali_titik(a,b):
    hasil1= a[0] * b[0] + a[1]*b[1]
    return hasil1

def kali_silang(a,b):
    hasil2=[]
    entri1= a[0] * b[1]
    hasil2.append(entri1)
    entri2= -(a[1] * b[0])
    hasil2.append(entri2)
    return hasil2

def satuan(n):
    hasil= []
    norm=(n[0]*2 + n[1]*2)**(1/2)
    entri1= n[0]/norm
    hasil.append(entri1)
    entri2= n[1]/norm
    hasil.append(entri2)
    return hasil

#main program
print('format: a=(a1,a2) dan b=(b1,b2)')
a=[]
b=[]
for i in range(2):
    a1=int(input(f'Masukkan nilai a{i+1} = '))
    a.append(a1)
for i in range(2):
    b1=int(input(f'Masukkan nilai b{i+1} = '))
    b.append(b1)
kt= kali_titik(a,b)
ks= kali_silang(a,b)
sa= satuan(a)
sb= satuan(b)

print(f'Hasil perkalian titik antara a dan b = {kt}')
print(f'Hasil perkalian silang antara a dan b = {ks}')
print(f'Vektor satuan dari vektor a = {sa}')
print(f'Vektor satuan dari vektor b = {sb}')
'''

#Tahun 2022 No. 1
'''
n= int(input('n(positif) = '))
angka=0
for i in range(1,n+1):
    angka+= len(str(i))
print(angka)
'''

#Tahun 2021 No. 1
'''
n= input('n = ')
while len(n)>1:
    jumlah= 1
    for i in n:
        jumlah= jumlah*int(i)
    n= str(jumlah)
print(jumlah)
'''

#Tahun 2021 No. 3
'''
n= int(input('n = '))
jumlah= 0
for i in range((2*n)+1):
    if i%2==0:
        jumlah+=i
print(jumlah)
'''

#Tahun 2021 No. 4
'''
a= float(input('a = '))
b= float(input('b = '))
tukar= a
a=b
b= tukar
print(f'a = {a}, b = {b}')
'''

