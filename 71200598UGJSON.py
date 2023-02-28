import json
jumlah = int(input("Masukkan Jumlah Barang = "))
kamus = {"total":0,"barang":[]}
total = 0
for i in range(jumlah):
    nama = input(f"Nama barang {i+1} = ")
    harga = int(input(f"Harga barang {i+1} = "))
    total += harga
    barang = dict()
    barang = {"nama":nama,"harga":harga}
    kamus["total"] = total
    kamus["barang"].append(barang)


with open("daftar.json","w") as f:
	json.dump(kamus,f)
