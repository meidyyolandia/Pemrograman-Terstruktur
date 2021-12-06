file = open("bil.txt", 'r')
file2 = open('hasilBil.txt', 'w')
data = ''
x = []
y = []
total = 0

for bil in file:
    mySplit= bil.split('|')
    sum = int(mySplit[0]) + int(mySplit[1].strip())
    data += str(sum) + '\n'

file2.write(data)
file2.close()
hasil = open('hasilBil.txt', 'r')
print(hasil.read())
hasil.close