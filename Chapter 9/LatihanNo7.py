print('==============================================================')
print('NIM'.ljust(8), 'NAMA MAHASISWA'.ljust(23), 'TGL LAHIR'.ljust(15), 'TEMPAT LAHIR')
print('--------------------------------------------------------------')

mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

for data in mhs:
       mySplit = data.split(':')
       nim = mySplit[0]
       nama = mySplit[1]
       tanggal = mySplit[2]
       mySplit2 = tanggal.split('-')
       thn = mySplit2[0]
       bln = mySplit2[1]
       tgl = mySplit2[2]
       tempat = mySplit[3]
       print(nim.ljust(8), nama.ljust(23), tgl, bln, thn.ljust(9), tempat)

print('--------------------------------------------------------------')