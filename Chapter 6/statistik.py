#Bagian A
def sum(*myData):
    penjumlahan = 0
    for data in myData:
        penjumlahan += data
    return penjumlahan

#Bagian B
def average(*myData):
    i = 0
    for data in myData:
        i += 1
    rata2 = sum(*myData)/i
    return rata2

#Bagian C
def maks(*myData):
    maximum = max(*myData)
    return maximum

#Bagian D
def minim(*myData):
    minimum = min(*myData)
    return minimum