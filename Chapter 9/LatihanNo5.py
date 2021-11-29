print('====================================================')
print('NIM'.ljust(8), 'NAMA'.ljust(13), 'N.MID'.ljust(8), 'N.UAS')
print('----------------------------------------------------')

nilai = [{'nim': 'A01', 'nama': 'Agustina', 'mid': 50, 'uas': 80},
         {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90},
         {'nim': 'A03', 'nama': 'Chicha', 'mid': 100, 'uas': 50},
         {'nim': 'A04', 'nama': 'Donna', 'mid': 20, 'uas': 100},
         {'nim': 'A05', 'nama': 'Fatimah', 'mid': 70, 'uas': 100}]

for data in range(len(nilai)):
    print(nilai[data]['nim'].ljust(8), end='')
    print(nilai[data]['nama'].upper().ljust(13), end='')
    print(str(nilai[data]['mid']).rjust(8), end='')
    print(str(nilai[data]['uas']).rjust(8))

print('----------------------------------------------------')