a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
a.insert(3, 10)
b.insert(2, 15)
a.append(4)
b.append(8)
a.sort()
b.sort()
c = a[0:7]
d = b[2:9]
e = []
for i in range(len(c)):
    e.insert(i, c[i]+d[i])
myTuple = tuple(e)
print(min(myTuple))
print(max(myTuple))
print(sum(myTuple))
myString = ('python adalah bahasa pemrograman yang menyenangkan')
print(set(myString))
myList = list(myString)
myList.sort()
print(myList)