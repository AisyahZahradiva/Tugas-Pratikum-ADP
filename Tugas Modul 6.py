#Menginputkan Matriks A
baris_A= int(input('masukkan ukuran baris matriks A: '))
kolom_A= int(input('masukkan ukuran kolom matriks A: '))
matriks_A=[]
for i in range(baris_A):
    baris= []
    for j in range(kolom_A):
        entri= int(input(f'Masukkan entri{i+1}{j+1} matriks A: '))
        baris.append(entri)
    matriks_A.append(baris)
for i in range(baris_A):
    for j in range(kolom_A):
        print(matriks_A[i][j], end=' ')
    print()

#Menginputkan Matriks B
baris_B= int(input('masukkan ukuran baris matriks B: '))
kolom_B= int(input('masukkan ukuran kolom matriks B: '))
matriks_B=[]
for i in range(baris_B):
    baris= []
    for j in range(kolom_B):
        entri= int(input(f'Masukkan entri{i+1}{j+1} matriks B: '))
        baris.append(entri)
    matriks_B.append(baris)
for i in range(baris_B):
    for j in range(kolom_B):
        print(matriks_B[i][j], end=' ')
    print()

#Menampilkan menu kalkulator matriks
while True:
    while True:
        print('''
Menu kalkulator matriks: 
1. Penjumlahan matriks 
2. Pengurangan matriks 
3. Perkalian matriks 
4. Determinan matriks 
5. Invers matriks
6. Transpose matriks
0. Berhenti''')
        
        pilihan= int(input('Pilih menu(1/2/3/4/5/6/0): '))
        if 0<=pilihan<=6:
            break
    #Perhitungan kalkulator 
    if pilihan == 0:
        break
    elif pilihan == 1: 
        if baris_A != baris_B or kolom_A != kolom_B:
            print('Tidak dapat menjumlahkan kedua matriks, karena ukuran kedua matriks berbeda.')
        else:
            matriks_penjumlahan=[]
            for i in range(baris_A):
                baris_penjumlahan= []
                for j in range(kolom_A):
                    entri_penjumlahan= matriks_A[i][j] + matriks_B[i][j]
                    baris_penjumlahan.append(entri_penjumlahan)
                matriks_penjumlahan.append(baris_penjumlahan)
            print('Hasil penjumlahan matriks A dan matriks B:  ')
            for i in range(baris_A):
                for j in range(kolom_A):
                    print(matriks_penjumlahan[i][j], end='  ')
                print()
            
    elif pilihan == 2: 
        if baris_A != baris_B or kolom_A != kolom_B:
            print('Tidak dapat mengurangkan kedua matriks, karena ukuran kedua matriks berbeda.')
        else:
            matriks_pengurangan=[]
            for i in range(baris_A):
                baris_pengurangan= []
                for j in range(kolom_A):
                    entri_pengurangan= matriks_A[i][j] - matriks_B[i][j]
                    baris_pengurangan.append(entri_pengurangan)
                matriks_pengurangan.append(baris_pengurangan)
            print('Hasil pengurangan matriks A dan mantriks B:  ')
            for i in range(baris_A):
                for j in range(kolom_A):
                    print(matriks_pengurangan[i][j], end='  ')
                print()
            
    elif pilihan == 3: 
        if kolom_A != baris_B:
            print('Tidak dapat mengalikan kedua matriks, karena ukuran kolom matriks A tidak sama dengan ukuran baris matriks B.')
        else:
            matriks_perkalian= []
            for i in range(baris_A): 
                baris_perkalian= []
                for j in range(kolom_B):
                    total= 0
                    for k in range(kolom_A):
                        total+=matriks_A[i][k]*matriks_B[k][j]
                    baris_perkalian.append(total)
                matriks_perkalian.append(baris_perkalian)
            print('Hasil perkalian matriks A dan matriks B:  ')
            for i in range(baris_A):
                for j in range(kolom_B):
                    print(matriks_perkalian[i][j], end='  ')
                print()

    elif pilihan == 4 or pilihan==5: 
        if baris_A != kolom_A and baris_B != kolom_B:
            print('Tidak dapat menghitung determinan kedua matriks, karena ukuran matriks tidak n*n.')
        elif baris_A == 2: 
            det_A= matriks_A[0][0]*matriks_A[1][1] -(matriks_A[0][1]*matriks_A[1][0])
        elif baris_A == 3:
            det_A= (matriks_A[0][0]*(matriks_A[1][1]*matriks_A[2][2] -(matriks_A[2][1]*matriks_A[1][2]))
                    -(matriks_A[0][1]*(matriks_A[1][0]*matriks_A[2][2] -(matriks_A[2][1]*matriks_A[1][2])))
                    + matriks_A[0][2]*(matriks_A[1][0]*matriks_A[2][1] -(matriks_A[2][0]*matriks_A[1][1])))       
        if baris_B == 2: 
            det_B= matriks_B[0][0]*matriks_B[1][1] -(matriks_B[0][1]*matriks_B[1][0])
        elif baris_B == 3:
            det_B= (matriks_B[0][0]*(matriks_B[1][1]*matriks_B[2][2] -(matriks_B[2][1]*matriks_B[1][2]))
                    -(matriks_B[0][1]*(matriks_B[1][0]*matriks_B[2][2] -(matriks_B[2][0]*matriks_B[1][2])))
                    +matriks_B[0][2]*(matriks_B[1][0]*matriks_B[2][1] -(matriks_B[2][0]*matriks_B[1][1])))       
        if pilihan ==4:
            if baris_B != kolom_B:
                print('Determinan dari matriks A adalah', det_A)
            elif baris_A != kolom_A:
                print('Determinan dari matriks B adalah', det_B)
            else:
                print('Determinan dari matriks A adalah', det_A)
                print('Determinan dari matriks B adalah', det_B)
        if pilihan==5:
            if baris_A == 2:
                invers_A= [[matriks_A[1][1]/det_A, -(matriks_A[0][1]/det_A)],
                           [-(matriks_A[1][0]/det_A), matriks_A[0][0]/det_A]]
                print('Invers dari matriks A:')
                for i in range(baris_A):
                    for j in range(kolom_A):
                        print(f'{invers_A[i][j]:.2f}', end='  ')
                    print()
            elif baris_A == 3:
                kofaktor_A= [[matriks_A[1][1]*matriks_A[2][2] -(matriks_A[1][2]*matriks_A[2][1]), -(matriks_A[1][0]*matriks_A[2][2] -(matriks_A[1][2]*matriks_A[2][0])), matriks_A[1][0]*matriks_A[2][1] -(matriks_A[1][1]*matriks_A[2][0])], 
                            [-(matriks_A[0][1]*matriks_A[2][2] -(matriks_A[0][2]*matriks_A[2][1])), matriks_A[0][0]*matriks_A[2][2] -(matriks_A[0][2]*matriks_A[2][0]), -(matriks_A[0][0]*matriks_A[2][1] -(matriks_A[0][1]*matriks_A[2][0]))], 
                            [matriks_A[0][1]*matriks_A[1][2] -(matriks_A[0][2]*matriks_A[1][1]), -(matriks_A[0][0]*matriks_A[1][2] -(matriks_A[0][2]*matriks_A[1][0])), matriks_A[0][0]*matriks_A[1][1] -(matriks_A[0][1]*matriks_A[1][0])]]
                transpose_A=[]
                for j in range(kolom_A): 
                    baris_tp_A= []
                    for i in range(baris_A):  
                        baris_tp_A.append(kofaktor_A[i][j])
                    transpose_A.append(baris_tp_A)
                invers_A= [[transpose_A[0][0]/det_A, transpose_A[0][1]/det_A, transpose_A[0][2]/det_A],
                           [transpose_A[1][0]/det_A, transpose_A[1][1]/det_A, transpose_A[1][2]/det_A],
                           [transpose_A[2][0]/det_A, transpose_A[2][1]/det_A, transpose_A[2][2]/det_A]]
                print('Invers dari matriks A:')
                for i in range(kolom_A):
                    for j in range(baris_A):
                        print(f'{invers_A[i][j]:.2f}', end='  ')
                    print()

            if baris_B == 2:
                invers_B= [[matriks_B[1][1]/det_B, -(matriks_B[0][1]/det_B)],
                           [-(matriks_B[1][0]/det_B), matriks_B[0][0]/det_B]]
                print('Invers dari matriks B:  ')
                for i in range(baris_B):
                    for j in range(kolom_B):
                        print(f'{invers_B[i][j]:.2f}', end='  ')
                    print()
            elif baris_B == 3:
                kofaktor_B= [[matriks_B[1][1]*matriks_B[2][2] -(matriks_B[1][2]*matriks_B[2][1]), -(matriks_B[1][0]*matriks_B[2][2] -(matriks_B[1][2]*matriks_B[2][0])), matriks_B[1][0]*matriks_B[2][1] -(matriks_B[1][1]*matriks_B[2][0])], 
                            [-(matriks_B[0][1]*matriks_B[2][2]) -(matriks_B[0][2]*matriks_B[2][1]), matriks_B[0][0]*matriks_B[2][2] -(matriks_B[0][2]*matriks_B[2][0]), -(matriks_B[0][0]*matriks_B[2][1] -(matriks_B[0][1]*matriks_B[2][0]))], 
                            [matriks_B[0][1]*matriks_B[1][2] -(matriks_B[0][2]*matriks_B[1][1]), -(matriks_B[0][0]*matriks_B[1][2] -(matriks_B[0][2]*matriks_B[1][0])), matriks_B[0][0]*matriks_B[1][1] -(matriks_B[0][1]*matriks_B[1][0])]]
                transpose_B=[]
                for j in range(kolom_B):  # Loop per kolom
                    baris_tp_B= []
                    for i in range(baris_B):  # Loop per baris
                        baris_tp_B.append(kofaktor_B[i][j])
                    transpose_B.append(baris_tp_B)
                invers_B= [[transpose_B[0][0]/det_B, transpose_B[0][1]/det_B, transpose_B[0][2]/det_B],
                           [transpose_B[1][0]/det_B, transpose_B[1][1]/det_B, transpose_B[1][2]/det_B],
                           [transpose_B[2][0]/det_B, transpose_B[2][1]/det_B, transpose_B[2][2]/det_B]]
                print('Invers dari matriks B:  ')
                for i in range(kolom_B):
                    for j in range(baris_B):
                        print(f'{invers_B[i][j]:.2f}', end='  ')
                    print() 
    
    elif pilihan == 6: 
        print('Transpose dari matriks A:')
        for j in range(kolom_A):
            for i in range(baris_A):
                print(f'{matriks_A[i][j]:<5}', end=' ')
            print()

        print('Transpose dari matriks B:')
        for j in range(kolom_B):
            for i in range(baris_B):
                print(f'{matriks_B[i][j]:<5}', end=' ')
            print()
    