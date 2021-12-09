from datetime import *
file = open('dataPinjaman.txt', 'a+')

def data():
    pinjam = datetime.date(datetime.now())
    pengembalian = pinjam + timedelta(days=7)
    kode = input('Masukkan Kode Member\t: ')
    nama = input('Masukkan Nama Member\t: ')
    buku = input('Masukkan Judul Buku\t\t: ')
    list = kode + '|' + nama + '|' + buku + '|' + str(pinjam) + '|' + str(pengembalian) + '\n'
    file.write(list)

data()

while True:
    ans = input('Ulangi input lagi (y/n)\t: ')
    if ans in ('Y', 'y'):
        data()
    elif ans in ('N', 'n'):
        file = open('dataPinjaman.txt', 'r')
        print(file.read())
        break
    else:
        print('Maaf invalid input')
        exit()

file.close()