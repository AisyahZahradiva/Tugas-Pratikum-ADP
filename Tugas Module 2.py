#menginput data diri berupa nama, umur, dan jenis kelamin 
nama= input('Nama: ')
umur= input('Umur: ')
jenis_kelamin= input('Jenis Kelamin(L/P): ')


#memilih kode maskapai
kode_maskapai= input('Kode Maskapai(3012/4015/4050): ')

if kode_maskapai == '3012' :
    tujuan= 'Padang-Jakarta'
    ekonomi= 800000
    bisnis= 850000
    fc= 900000
elif kode_maskapai == '4015' :
    tujuan= 'Padang-Batam'
    ekonomi= 500000
    bisnis= 550000
    fc= 700000
elif kode_maskapai == '4050':
    tujuan= 'Padang-Bandung'
    ekonomi= 700000
    bisnis= 750000
    fc= 850000
else :
    print('Maaf kode maskapai tidak tersedia:( ')

#menampilkan menu jenis maskapai
print('_'*100)
print('Kode Maskapai\t|  Tujuan Maskapai\t|  Kelas Ekonomi |  Kelas Bisnis\t|  Kelas First Class')
print('_'*100) 
print('\t3012\t|  Padang-Jakarta\t|  RP.800.000 \t |  RP.850.000\t\t|  RP.900.000')
print('\t4015\t|  Padang-Batam  \t|  RP.500.000 \t |  RP.550.000\t\t|  RP.700.000')
print('\t4050\t|  Padang-Bandung\t|  RP.700.000 \t |  RP.750.000\t\t|  RP.850.000')
print('_'*100)

kelas= input('Jenis Maskapai(Ekonomi/Bisnis/First Class): ')
jumlah_kursi= int(input('Jumlah Kursi: '))

if kelas == 'Ekonomi' and jumlah_kursi <= 3 :
    total= ekonomi * jumlah_kursi
elif kelas == 'Ekonomi' and jumlah_kursi > 3 :
    diskon= 0.2
    harga_mula= ekonomi * jumlah_kursi
    harga_diskon=  harga_mula * diskon 
    total= harga_mula - harga_diskon 
elif kelas == 'Bisnis' and jumlah_kursi <= 3 :
    total= bisnis * jumlah_kursi
elif kelas == 'Bisnis' and jumlah_kursi > 3 :
    diskon= 0.2
    harga_mula= bisnis * jumlah_kursi
    harga_diskon=  harga_mula * diskon 
    total= harga_mula - harga_diskon 
elif kelas == 'First Class' and jumlah_kursi <= 3 :
    total= fc * jumlah_kursi
else :
    diskon= 0.2
    harga_mula= fc * jumlah_kursi
    harga_diskon=  harga_mula * diskon 
    total= harga_mula - harga_diskon 


#menampilkan struk pemesanan
print('\t\n\t\n')
print('*STRUK PEMESANAN*')
print('1. Nama\t\t\t: ', nama)
print('2. Umur\t\t\t: ', umur)
print('3. Jenis Kelamin\t: ', jenis_kelamin)
print('-'*90)
print('4. Kode Maskapai\t: ', kode_maskapai, '(', tujuan, ')')
print('5. Jenis Maskapai\t: ', kelas)
print('6. Jumlah tiket\t\t: ', jumlah_kursi)
print('7. Total Harga\t\t: ', total)
print('Selamat Pemesanan Anda telah Berhasil:) ')




