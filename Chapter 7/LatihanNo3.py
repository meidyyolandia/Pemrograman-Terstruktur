sum = 0
i = 0

print("------------------------------")
print("---PROGRAM HITUNG RATA-RATA---")
print("------------------------------")

while True:
    try:
        n = int(input("Masukkan bilangan bulat : "))
        sum += n
        i += 1
        rata2 = sum/i
        answer = input("Lagi (y/n)? : ")
        if answer != "y":
            if answer == "n":
                break
            else:
                print("Please try again")
                break
    except ValueError:
        print("Bukan bilangan bulat")
print(" ")
print("Rata-ratanya adalah : ", rata2)