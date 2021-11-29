def bintang(n):
    spasi = 1+2*n-1
    for x in range(0, n):
        print(('*'*(2*x+1)).center(spasi))

def bintang2(n):
    spasi = 2+2*n-1
    for x in reversed(range(0, n)):
        print(('*'*(2*x+1)).center(spasi))

def bintang3(n):
    if n % 2 == 0:
        bintang(n/2)
        bintang2(n/2)
    else:
        bintang(n//2 + 1)
        bintang2(n//2)

bintang3(7)