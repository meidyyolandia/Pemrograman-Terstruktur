from datetime import  *
try:
    def diffDate(x):
        tgl = datetime.date(datetime.now())
        x = x.split('-')
        x = date(int(x[0]), int(x[1]), int(x[2]))
        hasil = x - tgl
        hasil = hasil.days
        return hasil

    file = open('dataPinjaman.txt', 'r')
    find = input('Masukkan Kode Member\t: ')
    skrg = datetime.date(datetime.now())
    akhir = False

    for x in file:
        data = x.split("|").copy()
        code = x.split("|")[0]
        if code in find:
            akhir = data
            break
    if akhir:
        maks = data[4].strip('\n')
        hari = diffDate(maks)
        if hari >= 7:
            telat = hari - 7
            denda = 'Rp. '+ str(telat * 2000)
        else:
            hari = 0
    print('\nData Mahasiswa'
          '\nKode Member\t\t\t\t\t: ', data[0],
          '\nNama Member\t\t\t\t\t: ', data[1],
          '\nJudul Buku\t\t\t\t\t: ', data[2],
          '\nTanggal Mulai Peminjaman\t: ', data[3],
          '\nTanggal Maks Peminjaman\t\t: ', maks,
          '\nTanggal Pengembalian\t\t: ', skrg,
          '\nTerlambat\t\t\t\t\t: ', str(telat) + ' hari',
          '\nDenda\t\t\t\t\t\t: ', denda)
except NameError:
    print('Maaf kode tidak ditemukan')