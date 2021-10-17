sum = 0
juml = 0
for i in range(100):
    bil = i+1
    if (bil % 2 != 0):
        sum += 1
        juml += bil
    print(bil)
print("Banyaknya bilangan ganjil :" + str(sum))
print("Jumlah seluruh bilangan :" +str(juml))