import os
import time
from termcolor import colored, cprint

#Menyimpan daftar film dan daftar menu ke dalam file text
with open('film.txt', 'w') as film:
    film.write('Ngeri-Ngeri Sedap\nKeluarga Cemara\nBlack Panther\nJumbo\nYour Name\n')
with open('makan.txt', 'w') as makan:
    makan.write('Popcorn salty size small,25000\nPopcorn salty size medium,50000\nPopcorn salty size large,70000\nFrench fries size small,15000\nFrench fries size medium,25000\nDonut all varian,15000\n')
with open('minum.txt', 'w') as minum:
    minum.write('Mineral Water,12000\nLemon Tea,20000\nLychee Tea,30000\nMilo Dinosaurs,40000\nBrown Sugar Milk Boba,35000\n')

#Fungsi untuk membaca file menu
def baca_file_menu(nama_file):
    hasil = []
    f = open(nama_file, 'r')
    semua = f.read()
    baris = ''
    for huruf in semua:
        if huruf != '\n':
            baris += huruf
        else:
            teks = ''
            angka = ''
            koma = False
            for h in baris:
                if h == ',':
                    koma = True
                elif not koma:
                    teks += h
                else:
                    angka += h
            hasil.append([teks, angka])
            baris = ''
    f.close()
    return hasil

#Fungsi untuk membaca file film
def baca_file_film(nama_file):
    hasil = []
    f = open(nama_file, 'r')
    isi = f.read()
    teks = ''
    for huruf in isi:
        if huruf != '\n':
            teks += huruf
        else:
            hasil.append(teks)
            teks = ''
    f.close()
    return hasil

#Fungsi untuk menampilkan kursi dipesan
def tampilkan_kursi_dengan_merah(kursi, baris_pilih, kolom_pilih):
    huruf_baris = ['A','B','C','D','E','F','G','H','I','J']
    print('    1  2  3  4  5  6  7  8  9  10')
    for i in range(10):
        print(huruf_baris[i], end=' | ')
        for j in range(10):
            if i == baris_pilih and j == kolom_pilih:
                print(colored('X', 'red'), end="  ")
            elif kursi[i][j] == 'X':
                cprint('X','green','on_red', end="  ")
            else:
                cprint('O','black','on_green',end="  ")
        print()

#Fungsi untuk memesan kursi
def pesan_kursi(kursi):
    huruf_baris = ['A','B','C','D','E','F','G','H','I','J']
    daftar_kursi_dipesan = []
    while True:
        tampilkan_kursi_dengan_merah(kursi, -1, -1)
        kode = input('Pilih kursi (misal A1 atau 0 untuk selesai): ')
        if kode == '0':
            if daftar_kursi_dipesan:
                print('\nKursi berhasil dipesan! Berikut layout final:')
                tampilkan_kursi_dengan_merah(kursi, -1, -1)
            return daftar_kursi_dipesan if daftar_kursi_dipesan else ['Tidak dipilih']
        
        if len(kode) < 2:
            print('Input salah.')
            continue
        huruf = kode[0].upper()
        angka = kode[1:]
        if not angka.isdigit():
            print('Input salah.')
            continue
        baris = -1
        for i in range(10):
            if huruf == huruf_baris[i]:
                baris = i
        kolom = int(angka) - 1
        if baris >= 0 and baris < 10 and kolom >= 0 and kolom < 10:
            if kursi[baris][kolom] == 'O':
                print('\nPreview Kursi Dipilih (Merah):')
                tampilkan_kursi_dengan_merah(kursi, baris, kolom)
                konfirmasi = input('Konfirmasi kursi ini? (Ya/Tidak): ').capitalize()
                if konfirmasi == 'Ya':
                    kursi[baris][kolom] = 'X'
                    kode_kursi = huruf + str(kolom + 1)
                    daftar_kursi_dipesan.append(kode_kursi)
                    print(f'Kursi {kode_kursi} berhasil ditambahkan.')
                else:
                    print('Silakan pilih kursi lagi.')
            else:
                print('Kursi sudah dipesan.')
        else:
            print('Kursi tidak valid.')

#Fungsi untuk memilih menu makanan/minuman
def pilih_menu(menu, nama):
    pilihan = []
    while True:
        print('\nMenu ' + nama + ':')
        for i in range(len(menu)):
            print(str(i + 1) + '. ' + menu[i][0] + ' - Rp' + menu[i][1])
        jawaban = input('Pilih nomor menu atau Selesai: ').capitalize()
        if jawaban == 'Selesai' :
            break
        elif jawaban.isdigit():
            nomor = int(jawaban)
            if 1 <= nomor <= len(menu):
                pilihan.append(menu[nomor - 1])
            else:
                print('Nomor tidak valid.')
        else:
            print('Input salah.')
    return pilihan

#Fungsi untuk loading
def loading():
    cprint('Loading', 'red', end='')
    for j in range(5):
        print('.', end='', flush=True)
        time.sleep(0.5)
    time.sleep(0.5)

#Program Utama
#Menyimpan daftar film dan menu
daftar_film = baca_file_film('film.txt')
daftar_makanan = baca_file_menu('makan.txt')
daftar_minuman = baca_file_menu('minum.txt')
kursi_per_hari = {}

while True:
    os.system('cls')
    print('\n' + '='*52)
    cprint(('EasyCinema : Pemesanan Film, Kursi & Makanan Praktis'),'black','on_yellow')
    print('='*52)

    #Memilih hari 
    hari = input('Masukkan hari (Senin-Minggu): ').capitalize()
    if hari =='Keyword':
        break
    weekday = ['Senin','Selasa','Rabu','Kamis','Jumat']
    weekend = ['Sabtu','Minggu']
    if hari in weekend:
        harga_film = 60000 
    elif hari in weekday: 
        harga_film = 40000

    if hari not in kursi_per_hari:
        kursi_per_hari[hari] = [['O' for _ in range(10)] for _ in range(10)]
    kursi = kursi_per_hari[hari]

    #Memilih film
    cprint('\n--- DAFTAR FILM ---','black','on_yellow')
    for i in range(len(daftar_film)):
        print(str(i + 1) + '. ' + daftar_film[i] + ' - Rp' + str(harga_film))

    pilih = 0
    while pilih < 1 or pilih > len(daftar_film):
        inp = input('Pilih nomor film: ')
        if inp.isdigit():
            pilih = int(inp)
            if pilih < 1 or pilih > len(daftar_film):
                print('Nomor film tidak ada.')
        else:
            print('Input tidak valid.')
    nama_film = daftar_film[pilih - 1]

    #Memilih kursi
    os.system('cls')
    posisi_kursi = pesan_kursi(kursi)
    time.sleep(5)

    total = 0
    if posisi_kursi != ['Tidak dipilih']:
        total= len(posisi_kursi) * harga_film

    #Memilih makanan
    os.system('cls')
    cprint('\n--- PESAN MAKANAN ---','black','on_yellow')
    makanan = pilih_menu(daftar_makanan, 'makanan')

    #Memilih minuman
    os.system('cls')
    cprint('\n--- PESAN MINUMAN ---','black','on_yellow')
    minuman = pilih_menu(daftar_minuman, 'minuman')

    os.system('cls')
    loading()
    os.system('cls')
    
    #Mencetak struk pemesanan
    print('='*52)
    cprint(('EasyCinema : Pemesanan Film, Kursi & Makanan Praktis'),'cyan', attrs=['bold'])
    print('='*52)
    cprint('\t\tSTRUK PEMESANAN', 'cyan', attrs=['bold'])
    print('='*52)
    
    print('\nFilm  : ' + nama_film + ' - Rp' + str(harga_film))
    print('Kursi : ' + ', '.join(posisi_kursi))

    cprint('\nMakanan:')
    if makanan:
        for item in makanan:
            print('- ' + item[0] + ': Rp' + item[1])
            total += int(item[1])
    else:
        print('-')

    cprint('\nMinuman:')
    if minuman:
        for item in minuman:
            print('- ' + item[0] + ': Rp' + item[1])
            total += int(item[1])
    else:
        print('-')

    print(colored('\nTotal Bayar: Rp' + str(total), 'yellow', attrs=['bold']))
    print(colored('Terima kasih sudah memesan!', 'green'))

    time.sleep(7)
    os.system('cls')