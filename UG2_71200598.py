kalimat = input("Masukkan kalimat: ")

kata = kalimat.split() 
jumlah_kata = len(kata)
kata_unik = set(kata)
jumlah_kata_unik = len(kata_unik)

print("Jumlah kata pada kalimat adalah", jumlah_kata)
print("Jumlah kata unik pada kalimat adalah", jumlah_kata_unik)

for word in kata_unik:
    print(word, "=", kata.count(word))