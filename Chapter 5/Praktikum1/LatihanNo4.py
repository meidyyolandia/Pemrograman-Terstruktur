kode = input("Masukan kode karyawan  :")
nama = input("Masukkan nama karyawan :")
gol = input("Masukkan golongan      :")
gajipokok = 0
potongan = 0
if gol == "A":
    gajipokok = 10000000
    potongan = 2.5
elif gol == "B":
      gajipokok = 8500000
      potongan = 2.0
elif gol == "C":
      gajipokok = 7000000
      potongan = 1.5
elif gol == "D":
      gajipokok = 5500000
      potongan = 1.0
hasil = gajipokok*(potongan/100)
print("====================================")
print("    STRUK RINCIAN GAJI KARYAWAN     ")
print("------------------------------------")
print("Nama Karyawan :" + nama + "(" + kode + ")")
print("Golongan      :" + gol)
print("------------------------------------")
print("Gaji Pokok    :" + "Rp." + str(gajipokok))
print("Potongan" + "(" + str(potongan) + "%):" + "Rp." + str(hasil))
print("------------------------------------")
print("Gaji Bersih   :" + "Rp." + str(gajipokok-hasil))