#Formasi bintang pertama
def starformation1(n):
    kolom = 1
    a = 0
    while (a < n):
        b = 0
        while (b < kolom):
            print("* ", end="")
            b += 1
        print("")
        a += 1
        kolom += 1

#Formasi bintang kedua
def starformation2(n):
    baris = 5
    a = 0
    while (a < baris):
        b = 0
        while (b < n):
            print("* ", end="")
            b += 1
        print("")
        a += 1
        n -= 1

#Formasi bintang ketiga
def starformation3(n):
    if n % 2 == 0:
        starformation1(n/2)
        starformation2(n/2)
    else:
        starformation1(n//2 + 1)
        starformation2(n//2)

print("---Formasi Bintang Pertama---")
starformation1(4)
print("----Formasi Bintang Kedua----")
starformation2(4)
print("----Formasi Bintang Ketiga---")
starformation3(7)