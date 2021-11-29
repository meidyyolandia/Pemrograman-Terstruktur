import random

def shuffleString(x, n):
    List = []
    juml = 0
    while juml < n:
        s = ''.join(random.sample(x,len(x)))
        if s not in List:
            List = List + [s]
            juml += 1
    print(List)

shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)