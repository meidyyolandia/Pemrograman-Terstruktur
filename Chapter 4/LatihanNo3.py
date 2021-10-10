import math
totalbensin = 66.25
kapasitastangki = 50
banyakpengisian = totalbensin/kapasitastangki
totalpengisian = math.ceil(banyakpengisian)
print("Jumlah minimal mengisi bensin hingga penuh = " + str(totalpengisian))