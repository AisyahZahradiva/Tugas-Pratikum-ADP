#Menginput jumlah baris dan kolom kursi bioskop
while True:
    baris= int(input("Masukkan jumlah baris kursi (minimal 4): "))
    kolom= int(input("Masukkan jumlah kolom kursi (minimal 4): "))
    if baris>=4 and kolom>=4 :
        print('\nBerikut layout kursi bioskop yang tersedia: ')
        break
    else:
        print("Maaf ukuran kursi bioskop minimal 4x4, silahkan coba lagi:(")
jumlah_kursi=baris*kolom
 

#menampilkan layout kursi bioskop
nomor_kursi=1
for i in range(baris):
    for j in range(kolom):
        print(f'{nomor_kursi:<2}', end='  ')
        nomor_kursi+=1
    print(' ')


#Memilih nomor kursi pertama
nomor_kursi=1
while True:
    kursi_dipesan1=int(input('Pilih nomor kursi yang dipesan pertama(atau 0 untuk selesai): '))
    if kursi_dipesan1 == 0: 
        print('Terima kasih telah memesan tiket!:)')
        break
    if 0>kursi_dipesan1 or kursi_dipesan1>jumlah_kursi:
        print('Nomor kursi tidak valid! Masukkan nomor kursi yang tersedia')
    else:
        print(f'Kursi {kursi_dipesan1} berhasil dipesan:)\n')
        break   
        
for i in range(baris):
    for j in range(kolom):
        if nomor_kursi==kursi_dipesan1: 
            print('X', end='  ')
            nomor_kursi+=1
        else:
            print(f'{nomor_kursi:<2}', end='  ')
            nomor_kursi+=1
    print(' ')
    

#Memilih nomor kursi kedua--------------------
nomor_kursi=1    
while True:
    kursi_dipesan2=int(input('Pilih nomor kursi yang dipesan kedua(atau 0 untuk selesai): '))
    if kursi_dipesan2 == 0: 
        print('Terima kasih telah memesan tiket!:)')
        break
    if 0>kursi_dipesan2 or kursi_dipesan2>jumlah_kursi:
        print('Nomor kursi tidak valid! Masukkan nomor kursi yang tersedia')
    elif kursi_dipesan2== kursi_dipesan1:
        print('Maaf kursi ini sudah dipesan! Silahkan pilih kursi lain ')
    else:
        print(f'Kursi {kursi_dipesan2} berhasil dipesan:)\n')
        break

for i in range(baris):
    for j in range(kolom):
        if nomor_kursi==kursi_dipesan1: 
            print('X', end='  ')
            nomor_kursi+=1
        elif nomor_kursi==kursi_dipesan2:
            print('X', end='  ')
            nomor_kursi+=1
        else:
            print(f'{nomor_kursi:<2}', end='  ')
            nomor_kursi+=1
    print(' ')


#Memilih nomor kursi ketiga
nomor_kursi=1
while True:    
    kursi_dipesan3=int(input('Pilih nomor kursi yang dipesan ketiga(atau 0 untuk selesai): '))
    if kursi_dipesan3 == 0: 
        print('Terima kasih telah memesan tiket!:)')
        break
    if 0>kursi_dipesan3 or kursi_dipesan3>jumlah_kursi:
        print('Nomor kursi tidak valid! Masukkan nomor kursi yang tersedia')
    elif kursi_dipesan3==kursi_dipesan1 or kursi_dipesan3==kursi_dipesan2 :
        print('Maaf kursi ini sudah dipesan! Silahkan pilih kursi lain ')
    else:
        print(f'Kursi {kursi_dipesan3} berhasil dipesan:)\n')
        break
    
for i in range(baris):
    for j in range(kolom):
        if nomor_kursi==kursi_dipesan1: 
            print('X', end='  ')
            nomor_kursi+=1
        elif nomor_kursi==kursi_dipesan2:
            print('X', end='  ')
            nomor_kursi+=1
        elif nomor_kursi==kursi_dipesan3:
            print('X', end='  ')
            nomor_kursi+=1
        else:
            print(f'{nomor_kursi:<2}', end='  ')
            nomor_kursi+=1
    print(' ')
    

print(f'\nTiket yang berhasil di pesan: {kursi_dipesan1}, {kursi_dipesan2},{kursi_dipesan3}')