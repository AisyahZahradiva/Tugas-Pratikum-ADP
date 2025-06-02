#Data awal 10 buku dalam file text
with open('inventaris_buku.txt','w') as file: 
    file.write('9789790339378, Kalkulus Jilid 1 Edisi 9, Edwin J. Purcell. dkk, 10, 400000, 500000') 
    file.write('\n9786232967342, Pengantar Algoritma dan Pemrograman dengan Python, Syaiful Anam. dkk, 11, 30000, 50000') 
    file.write('\n9786020655030, Laut Bercerita, Leila S. Chudori, 6, 120000, 155000') 
    file.write('\n9786022202232, Attack on Titan Vol. 1 (Terjemahan), Hajime Isayama, 3, 40000, 60000') 
    file.write('\n9786020635766, Negeri 5 Menara, Ahmad Fuadi, 5, 100000, 140000') 
    file.write('\n9786022201563, Doraemon Vol. 1, Fujiko F. Fujio, 4, 40000, 55000')
    file.write('\n9786028811361, Laskar Pelangi, Andrea Hirata, 2, 110000, 150000') 
    file.write('\n9786239607456, Harga Sebuah Percaya, Tere Liye, 12, 95000, 120000') 
    file.write('\n9789792055856, Naruto Vol. 1: Uzumaki Naruto, Masashi Kishimoto, 1, 50000, 75000') 
    file.write('\n9786024807863, Tokyo Ghoul:re Vol. 9,  Sui Ishida, 9, 55000, 70000') 

#Mengubah informasi buku dalam file text ke dictionary
kumpulan_buku= []
with open('inventaris_buku.txt', 'r') as file:
    for baris in file:
        (isbn, judul, penulis, stok, beli, jual) = baris.split(",")
        buku= {'ISBN': isbn,'Judul': judul,
                'Penulis': penulis,
                'Stok': int(stok),
                'Harga beli': int(beli),
                'Harga jual': int(jual)}
        kumpulan_buku.append(buku)

#Menghitung potensi keuntungan tertinggi dan terendah
with open('Laporan_inventaris.txt','w') as file:
    for buku in kumpulan_buku:
        keuntungan= (buku['Harga jual'] - buku['Harga beli']) * buku['Stok']
        buku['Potensi keuntungan']= keuntungan 
        baris= buku
        for key in baris:
            file.write(f'{baris[key]},')
        file.write('\n')

#Menentukan potensi keuntungan tertinggi dan terendah
potensi_tertinggi= potensi_terendah= baris['Potensi keuntungan']
for buku in kumpulan_buku:
    potensi = buku['Potensi keuntungan']
    if potensi > potensi_tertinggi:
        potensi_tertinggi = potensi
        tertinggi = buku['Judul']
    if potensi < potensi_terendah:
        potensi_terendah = potensi
        terendah = buku['Judul']
print(f'Buku dengan potensi keuntungan tertinggi:{tertinggi}')
print(f'Dengan potensi keuntungan yaitu {potensi_tertinggi}')
print(f'Buku dengan potensi keuntungan terendah:{terendah}')
print(f'Dengan potensi keuntungan yaitu {potensi_terendah}')

#Menghitung nilai inventaris
total= 0
with open('Laporan_inventaris.txt','r') as file: 
    for buku in kumpulan_buku:
        total += (buku['Stok'] * buku['Harga beli']) 
print(f'Total nilai inventaris yaitu {total}')

#Menampilkan daftar buku dengan stok kurang dari 5
print('Buku yang perlu di re-stok: ')
for buku in kumpulan_buku:
    if buku['Stok'] < 5:
        print(f' - {buku['Judul']}, stok tersisa {buku['Stok']}')