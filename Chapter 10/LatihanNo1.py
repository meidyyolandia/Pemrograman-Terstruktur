try:
    text = "bilangan.txt"

    def read(bilangan):
        file = open(bilangan, 'r')
        ganjil = 0
        genap = 0
        for x in file:
            if int(x) % 2 == 0:
                genap += 1
            elif int(x) % 2 == 1:
                ganjil += 1
        file.close()
        result = {"ganjil" : ganjil, "genap" : genap}
        return result

    print("Banyaknya bilangan ganjil: ", read(text).get('ganjil'))
    print("Banyaknya bilangan genap: ", read(text).get('genap'))

except FileNotFoundError:
    print('File tidak ditemukan')