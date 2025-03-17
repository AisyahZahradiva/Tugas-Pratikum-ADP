print('Permainan Tebak Tembakan')

#menentukan batas angka dan angka duarr
print('Pemain 1')
batas= int(input('Masukkan Batas Angka Positif: '))
tembak= int(input('Pilih Angka Kelipatan Tembakan: '))
i=1


#mencetak deretan angka
while i < batas+1:
    sisa= i%tembak
    if sisa == 0:
        print('DOR', end='  ')
    else:
        print(i, end='  ')
    i=i+1

print('\n')

#mementukan angka untuk menebak
print('Pemain 2')
print('Kamu harus menebak angka yang bukan tembakan, Semangatt!!')
tebak= int(input(f'Masukkan angka yang kamu tebak dari 1-{batas}: '))


#mencetak kebenaran dari tebakan pemain 2
if tebak % tembak == 0 and 1 <= tebak <= batas:
    print('Yahhh Kamu salah menebak, kalah dehh :(')
elif 1 <= tebak <= batas :
    print('Wahhh Selamat kamu menebak dengan benar, Kerenn Kamu Menang ;)') 
else:
    print(f'Maaf kamu harus mengulang menebak karena {tebak} berada di luar batasan angka yang tersedia')
print('\nPermainan Selesai')
print('Terimakasih telah memainkan permainan ini<3')















