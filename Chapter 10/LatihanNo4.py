file = open('dataMhs.txt', 'r')
find = input('Masukkan NIM yang mau dicari : ')

for x in file:
    data = x.split("|").copy()
    hasil = x.split("|")[0]
    if hasil in find:
        print('Data Mahasiswa')
        print('NIM\t\t:', data[0])
        print('Nama\t:', data[1])
        print('Alamat\t:', data[2])
        break
    else:
        print('Data mahasiswa tidak ditemukan')
        break