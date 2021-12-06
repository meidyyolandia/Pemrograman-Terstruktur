try:
    file = open('dataMhs.txt', 'r')
    line = file.readlines()
    data = []

    for x in range (len(line)):
        myData = {}
        isi = line[x].replace('\n', '')
        dataSplit = isi.split("|")
        dataMhs = {'NIM':dataSplit[0], 'nama':dataSplit[1], 'alamat':dataSplit[2]}
        data += [dataMhs]

    print('dataMhs = ', data)

except FileNotFoundError:
    print('File tidak ditemukan')