try:
    file = input('Masukkan nama file : ')
    n = int(input('Masukkan banyak huruf yang akan digeser : '))

    o = open(file, 'r')
    r = o.read()
    myList = list(r)
    list = ''

    for ps in r:
        if ps == ' ':
            list += ps
        elif ps.isupper():
            list += chr((ord(ps) - n - 65) % 26 + 65)
        else:
            list += chr((ord(ps) - n - 97) % 26 + 97)

    file2 = open('sandiCaesar2.txt', 'w')
    tulis = ''.join(list)
    file2.write(tulis)
    print('Hasil penyandiannya adalah : ' + '\n', tulis)
    o.close()
    file2.close()
except ValueError:
    print('Maaf invalid input')