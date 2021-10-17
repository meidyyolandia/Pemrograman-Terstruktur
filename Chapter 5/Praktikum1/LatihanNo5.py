kode = input("Masukan kode karyawan               :")
nama = input("Masukkan nama karyawan              :")
gol = input("Masukkan golongan                   :")
status = input("Masukkan status (1:menikah, 2: blm) :")
tunjMenikah = 0
tunJAnak = 0
jumlAnak = 0
if status == "1":
    jumlAnak = input("Masukkan jumlah anak:")
else:
    status= "Belum Menikah"
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
if status == "1":
    tunjMenikah = gajipokok*0.1
if int(jumlAnak > 0):
    inttunjAnak = jumlAnak*0.05
elif jumlAnak == "0":
    tunjAnak = 0
gajikotor = gajipokok + tunjMenikah + tunjAnak
hasil = gajipokok*(potongan/100)
print("====================================")
print("    STRUK RINCIAN GAJI KARYAWAN     ")
print("------------------------------------")
print("Nama Karyawan     :" + nama + "(" + kode + ")")
print("Golongan          :" + gol)
print("Status Menikah    :" + status)
print("Jumlah Anak       :" + str(jumlAnak))
print("------------------------------------")
print("Gaji Pokok        :" + "Rp." + str(gajipokok))
print("Tunjangan Menikah :" + "Rp." + str(tunjMenikah))
print("Tunjangan Anak    :" + "Rp." + str(tunjAnak))
print("Gaji Pokok        :" + "Rp." + str(gajipokok))
print("------------------------------------ +")
print("Gaji Kotor        :" + "Rp." + str(gajikotor))
print("Potongan" + "(" + str(potongan) + "%):" + "Rp." + str(hasil))
print("------------------------------------ -")
print("Gaji Bersih   :" + "Rp." + str(gajipokok-hasil))