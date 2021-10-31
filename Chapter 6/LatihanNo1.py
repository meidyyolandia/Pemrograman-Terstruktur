print("----------TRIPLE PYTHAGORAS--------")
print("-----------TRUE or FALSE-----------")

def ispythagoras(a, b, c):
    if c == (a**2 + b**2) ** 0.5:
        hasil = True
    else:
        hasil = False
    if hasil is True:
        print('a =', a, ', b =', b, ', c =', c, '  -> TRUE')
    else:
        print('a =', a, ', b =', b, ', c =', c, '  -> FALSE')

ispythagoras(3, 4, 5)
ispythagoras(5, 9, 12)
ispythagoras(8, 6, 10)
ispythagoras(7, 8, 11)