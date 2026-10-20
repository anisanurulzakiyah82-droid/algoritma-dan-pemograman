harga = float(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah barang: "))

total = harga * jumlah
if total >= 100000:
    diskon = total * 0.10
else:
    diskon = 0

bayar = total - diskon

print("total belanja: ", total)
print("diskon: ", diskon)
print("total pembayaran: ", bayar)