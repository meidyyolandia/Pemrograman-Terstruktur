nilaiBIndo = int(input("Masukkan nilai Bhs Indonesia :"))
nilaiIPA = int(input("Masukkan nilai IPA           :"))
nilaiMat = int(input("Masukkan nilai Matematika    :"))
if (nilaiBIndo > 60) and (nilaiIPA > 60) and (nilaiMat > 70):
    print("Syarat Kelulusan : LULUS")
elif (nilaiBIndo < 60) and (nilaiIPA < 60) and (nilaiMat < 70):
    print("Syarat Kelulusan :TIDAK LULUS")
elif (nilaiBIndo < 0) and (nilaiIPA < 0) and (nilaiMat < 0):
    print("Maaf input ada yang tidak valid")
elif (nilaiBIndo > 100) and (nilaiIPA > 100) and (nilaiMat > 100):
    print("Maaf input ada yang tidak valid")
else :
    print("Maaf input ada yang tidak valid")
