import math
nc = 5
rc = 3
xc = nc - rc

np = 10
rp = 7
xp = np - rp

def faktorial(n):
    hasil = 1
    for i in range (2, n+1):
        hasil *= i
    return hasil

kombinasi = math.factorial(nc) / (math.factorial(xc) * math.factorial(rc))
permutasi = math.factorial(np) / math.factorial(xp)
print("Nilai dari C(", nc, ",", rc, ") adalah ", kombinasi)
print("Nilai dari P(", np, ",", rp, ") adalah ", permutasi)