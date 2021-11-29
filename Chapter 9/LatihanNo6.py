print('==============================================================')
print('NIM'.ljust(8), 'NAMA'.ljust(13), 'N.MID'.ljust(8), 'N.UAS'.ljust(8), 'N.AKHIR'.ljust(10), 'STATUS')
print('--------------------------------------------------------------')

nilai = [{'nim': 'A01', 'nama': 'Agustina', 'mid': 50, 'uas': 80},
         {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90},
         {'nim': 'A03', 'nama': 'Chicha', 'mid': 100, 'uas': 50},
         {'nim': 'A04', 'nama': 'Donna', 'mid': 20, 'uas': 100},
         {'nim': 'A05', 'nama': 'Fatimah', 'mid': 70, 'uas': 100}]

for data in nilai:
    nilaiAkhir = (data['mid'] + 2*data['uas'])/3
    if nilaiAkhir >= 60:
        status = 'LULUS'
    else:
        status = 'TIDAK LULUS'
    print(data['nim'].ljust(8),data['nama'].ljust(13),str(data['mid']).ljust(8),str(data['uas']).ljust(8),str(round(nilaiAkhir,2)).ljust(10), status)
print('--------------------------------------------------------------')