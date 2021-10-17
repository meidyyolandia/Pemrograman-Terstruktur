#Range input nilai adalah 0 - 100
nilaiBIndo = int(input("Masukkan nilai Bhs Indonesia :"))
nilaiIPA = int(input("Masukkan nilai IPA           :"))
nilaiMat = int(input("Masukkan nilai Matematika    :"))
if (nilaiBIndo > 60) and (nilaiIPA > 60) and (nilaiMat > 70):
    print("Syarat Kelulusan : LULUS")
elif (nilaiBIndo < 60) and (nilaiIPA < 60) and (nilaiMat < 70):
    print("Syarat Kelulusan :TIDAK LULUS")
