nama_barang = str(input("Nama barang: "))
harga = float(input("Harga barang: "))
jumlah = int(input("jumlah pembelian: "))
subtotal = harga * jumlah

if subtotal >= 200000:
    diskon = subtotal * 0.05
else:
    diskon = 0

total = subtotal - diskon

print("\n=== STRUK PEMBELIAN ===")
print("Nama barang:", nama_barang)
print("Subtotal:", subtotal)
print("Total pembayaran:", total)