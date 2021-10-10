import math
jarak_kotaab = 125
kecepatan_kotaab = 62
jarak_kotabc = 256
kecepatan_kotabc = 70
waktuberangkat = 6.00
istirahatb = 45
waktu_kotaab = int(jarak_kotaab/kecepatan_kotaab)*60
waktu_kotabc = int(jarak_kotabc/kecepatan_kotabc)*60
totalmenit = waktu_kotabc+istirahatb+waktu_kotabc
totaljam = totalmenit/60
waktuawal = math.floor(waktuberangkat+totaljam)
waktuakhir = math.floor((waktuberangkat+totaljam) % 1 /0.25*15)
print("Perkiraan Pak Amir sampai di kota C = " + str(waktuawal) + '.' + str(waktuakhir))