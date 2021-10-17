sum = 0
bil = 0
for i in range(100):
    if (bil % 2 != 0):
        print(bil)
        sum += 1
    bil += 1
print("Banyaknya bilangan ganjil :" + str(sum))