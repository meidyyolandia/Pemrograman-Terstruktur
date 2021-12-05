file = open("dataMhs.txt", 'a')

def dataMhs():
    NIM = input('Masukkan NIM : ')
    nama = input('Masukkan Nama Mhs : ')
    alamat = input('Masukkan Alamat : ')
    data = NIM + '|' + nama + '|' + alamat + '\n'
    file.write(data)

dataMhs()

while True:
    repeat = input('Ulangi input lagi (y/n)? ')
    if repeat in ('Y', 'y'):
        dataMhs()
    elif repeat in ('N', 'n'):
        buka = open('dataMhs.txt', 'r')
        for i in buka:
            print(i)
            file.close()
        break