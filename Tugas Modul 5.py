#Menginput data yang diperlukan
jumlah_mahasiswa= int(input("Masukkan jumlah mahasiswa pratikum ADP: "))
nama_mahasiswa=[]
nilai_pretest=[]
nilai_postest=[]
nilai_makalah=[]
for i in range(jumlah_mahasiswa):
    nama= input(f"Masukkan nama mahasiswa ke-{i+1}: ")
    nama_mahasiswa.append(nama)
    nilai1= int(input(f"Masukkan nilai pretest mahasiswa ke-{i+1}: "))
    nilai_pretest.append(nilai1)
    nilai2= int(input(f"Masukkan nilai postest mahasiswa ke-{i+1}: "))
    nilai_postest.append(nilai2)
    nilai3= int(input(f"Masukkan nilai makalah mahasiswa ke-{i+1}: "))
    nilai_makalah.append(nilai3)

#Menghitung nilai akhir
nilai_akhir=[]
for i in range(jumlah_mahasiswa):
    pretest= nilai_pretest[i] * 0.4
    postest= nilai_postest[i] * 0.4
    makalah= nilai_makalah[i] * 0.2
    akhir= pretest + postest + makalah
    nilai_akhir.append(akhir)

#Menghitung rata-rata nilai akhir kelas
jumlah_nilai_akhir=0
for i in range(jumlah_mahasiswa):
    jumlah_nilai_akhir+=nilai_akhir[i]
rata_rata_nilai_akhir= jumlah_nilai_akhir/jumlah_mahasiswa

#Mencari nilai tertinggi dan terendah serta nilai diatas rata-rata
batas= jumlah_mahasiswa
while batas>1:
    for i in range(batas-1):
        if nilai_akhir[i]>nilai_akhir[i+1]:
            tukar_1= nilai_akhir[i]
            nilai_akhir[i]= nilai_akhir[i+1]
            nilai_akhir[i+1]= tukar_1
            tukar_2= nama_mahasiswa[i]
            nama_mahasiswa[i]= nama_mahasiswa[i+1]
            nama_mahasiswa[i+1]= tukar_2
    batas= batas-1

#Menampilkan tabel nama mahasiswa dan nilai akhir
print('\n')
print("|\tNama Mahasiswa", end="\t")
print("|\tNilai Akhir\t|")
for i in range(jumlah_mahasiswa):
    print(f"|\t{nama_mahasiswa[i]}", end="\t\t")
    print(f"|\t{nilai_akhir[i]}\t\t|")

#Menampilkan rata-rata nilai akhir kelas serta nilai tertinggi dan terendah
print(f"Rata-rata nilai akhir kelas: {rata_rata_nilai_akhir}")
print(f"Mahasiswa yang mendapat nilai tertinggi: {nama_mahasiswa[-1]}")
print(f"Mahasiswa yang mendapat nilai terendah: {nama_mahasiswa[0]}")

#Menampilkan nama mahasiswa yang nilai akhir diatas rata-rata
print("Mahasiswa dengan nilai akhir di atas rata-rata kelas: ", end="")
for i in range(jumlah_mahasiswa):
    if nilai_akhir[i]>rata_rata_nilai_akhir:
        print(nama_mahasiswa[i], end=", ")

