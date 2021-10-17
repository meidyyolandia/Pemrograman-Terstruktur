from random import randint
bil = randint(0,10)
print("--------------------Hai, saya Mr. Lappie---------------------")
print("~ Saya telah memilih sebuah bilangan bulat antara 0 s/d 100 ~")
print("--------------------Silahkan ditebak ya!!!-------------------")
while True:
    answer = input("Tebakkan Anda : ")
    if (int(answer) < bil):
        print()
        print("Hehehe... Bilangan tebakan anda terlalu kecil")
        print()
    if (int(answer) > bil):
        print()
        print("Hehehe... Bilangan tebakan anda terlalu besar")
        print()
    if (int(answer) == bil):
        print("-----------------Bilangan tebakan anda BENAR----------------")
        print("-----------------------SELAMAT YA!!!------------------------")
        break