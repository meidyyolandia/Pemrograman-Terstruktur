import math
biayasewa = 200000
biayaberikutnya = 10000
waktuawalbiayasewa = 12
jam_awalmenyewa = 6.00
jam_akhirmenyewa = 23.50
durasiwaktu = math.ceil(jam_akhirmenyewa-jam_awalmenyewa)
lamawaktuberikutnya =  durasiwaktu - waktuawalbiayasewa
biayasewaberikutnya = lamawaktuberikutnya * biayaberikutnya
totalbiaya = biayasewa + biayasewaberikutnya
print("Total tarif yang harus dibayarkan kepada rental mobil = " + str(totalbiaya))