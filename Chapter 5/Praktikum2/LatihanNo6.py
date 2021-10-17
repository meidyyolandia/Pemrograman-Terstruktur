from random import randint
bil = randint(0,10)
score = 100
print("--------------------Hai, saya Mr. Lappie---------------------")
print("~ Saya telah memilih sebuah bilangan bulat antara 0 s/d 100 ~")
print("--------------------Silahkan ditebak ya!!!-------------------")
print("-------------Kamu memiliki 100 poin untuk bermain------------")
print("-------Jika kamu salah menebak, poinmu akan berkurang 2------")
while True:
    print("[" + str(score) + "]")
    answer = input("Tebakkan Anda : ")
    if (int(answer) < bil):
        print()
        print("Hehehe... Bilangan tebakan anda terlalu kecil")
        print("Score -2")
        print()
        score -= 2
    if (int(answer) > bil):
        print()
        print("Hehehe... Bilangan tebakan anda terlalu besar")
        print("Score -2")
        print()
        score -= 2
    if(score <= 0):
        print("Poinmu sudah habis, silahkan mencoba lain waktu")
        break
    if (int(answer) == bil):
        print("-----------------Bilangan tebakan anda BENAR----------------")
        print("-----------------------SELAMAT YA!!!------------------------")
        print("Score Anda : " + str(score))
        break