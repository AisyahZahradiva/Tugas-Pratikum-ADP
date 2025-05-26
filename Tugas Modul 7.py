#Fungsi menginput data
def input_data():
    n= int(input('Masukkan jumlah mahasiswa: '))
    data= []
    for i in range(n):
        print(f'\nData mahasiswa ke-{i+1}: ')
        nama= input('Nama: ')
        nim= (input('NIM: '))
        uts= float(input('Nilai UTS: '))
        uas= float(input('Nilai UAS: '))
        tugas= float(input('Nilai tugas: '))
        nilai_akhir= 0
        peringkat= i+1
        data.append([nama,nim,uts,uas,tugas,nilai_akhir,peringkat])
    print('\n')
    return data

#Fungsi menghitung nilai akhir
def menghitung_nilai_akhir(data):
    for i in data:
        nilai_akhir = 0.35 * i[3] + 0.35 * i[2] + 0.30 * i[4]
        i[5] = nilai_akhir

#Fungsi menghitung rata-rata
def perhitungan_rata_rata(data,indeks):
    total= 0
    for i in data:
        total= total + i[indeks]
        rata_rata= total/len(data) 
    return rata_rata 

#Fungsi menentukan peringkat
def menentukan_peringkat(data):
    batas = len(data)
    for i in range(batas):
        peringkat = 1
        for j in range(batas):
            if data[j][5] > data[i][5]:  # nilai_akhir mahasiswa j lebih tinggi dari i
                peringkat += 1
        data[i][6]= peringkat

#Fungsi mengurutkan peringkat
def mengurutkan_peringkat(data):
    batas = len(data)
    for i in range(batas-1):
        for j in range(batas-1-i):
            if data[j][6] > data[j+1][6]:
                tukar= data[j]
                data[j]= data[j+1] 
                data[j+1]= tukar 

# Fungsi menampilkan tabel
def menampilkan_tabel(data, rata_rata_uts, rata_rata_uas, rata_rata_tugas, rata_rata_akhir):
    print("-" * 100)
    print("\n| {:<15} | {:<10} | {:<10} | {:<10} | {:<10} | {:<13} | {:<9} |".format(
        "Nama", "NIM", "UTS", "UAS", "Tugas", "Nilai Akhir", "Peringkat"))
    print("-" * 100)
    for i in data:
        print("| {:<15} | {:<10} | {:<10.2f} | {:<10.2f} | {:<10.2f} | {:<13.2f} | {:<9} |".format(
            i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
    print("-" * 100)
    print("| {:<15} | {:<10} | {:<10.2f} | {:<10.2f} | {:<10.2f} | {:<13.2f} | {:<9} |".format(
        "", "Rata-rata", rata_rata_uts, rata_rata_uas, rata_rata_tugas, rata_rata_akhir,''))
    print("-" * 100)

# Program utama
data = input_data()
menghitung_nilai_akhir(data)
rata_rata_uts = perhitungan_rata_rata(data, 2)
rata_rata_uas = perhitungan_rata_rata(data, 3)
rata_rata_tugas = perhitungan_rata_rata(data, 4)
rata_rata_akhir = perhitungan_rata_rata(data, 5)
menentukan_peringkat(data)
mengurutkan_peringkat(data)
menampilkan_tabel(data, rata_rata_uts, rata_rata_uas, rata_rata_tugas, rata_rata_akhir)
