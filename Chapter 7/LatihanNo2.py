nama = input("Masukkan nama file: ")
def data():
    file.write(input("Data yang mau ditambahkan: "))
    file.write(" ")
    global answer
    answer = input("Mau lagi (y/n) : ")
try:
    file = open(nama, "a")
    data()
    while True:
        if answer == "y":
            data()
        if answer == "n":
            file.close()
            break
        else:
            print("Please try again")
            break
except PermissionError:
    print("Izin ditolak")
except FileNotFoundError:
    print("File atau direktori tidak ditemukan")
except OSError:
    print("E R R O R")