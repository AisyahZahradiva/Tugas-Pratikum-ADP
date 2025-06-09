import os
import time
from termcolor import cprint

#Fungi menampilkan ikon aplikasi
def ikon():
    for i in range(2):
        cprint('     ', 'red', 'on_light_red', end='')
        print('  ', end='')
        cprint('     ', 'green', 'on_light_green')
    print('')
    for i in range(2):
        cprint('     ', 'blue', 'on_light_blue', end='')
        print('  ', end='')
        cprint('     ', 'yellow', 'on_light_yellow')

#Program utama
for i in range(5):
    os.system('cls')
    ikon()

    print('\nMohon tunggu sebentar, membuka aplikasi Microsoft...')
    cprint('Loading', 'red', end='')

    for j in range(3):
        print('.', end='', flush=True)
        time.sleep(0.5)
    time.sleep(0.5)

os.system('cls')
ikon()

cprint('\nSelesai membuka Microsoft!', 'green')
cprint('Selamat datang di Microsoft.\n', 'green')