try:
    nama = input("Masukkan nama files : ")
    print("Isi file", nama, "adalah : ")
    print(" ")
    file = open(nama, "r")
    print(file.read())
except FileNotFoundError:
    print("File tidak ditemukan")