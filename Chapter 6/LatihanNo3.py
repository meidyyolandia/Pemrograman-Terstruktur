def faktorial(n):
    hasil = 1
    for i in range (1, n+1):
        hasil *= i
    return hasil

kombinasi = faktorial(5) / (faktorial(5-3) * faktorial(3))
permutasi = faktorial(10) / faktorial(10-7)
print("Nilai dari C(5, 3) adalah ", kombinasi)
print("Nilai dari P(10, 7) adalah ", permutasi)