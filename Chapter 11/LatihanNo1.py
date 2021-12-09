from datetime import *
def diffDate(x):
    try:
        tgl = datetime.date(datetime.now())
        x = x.split('-')
        x = date(int(x[0]), int(x[1]), int(x[2]))
        hasil = x - tgl
        hasil = hasil.days
        print(hasil)
    except ValueError:
        print('Maaf invalid input')
    return hasil

diffDate('20-12-16')