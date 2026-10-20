print("harga barang: ")
print("1. nama pdl - Rp.15.000")
print("2. logo - Rp.7000")
print("3. lokasi - Rp.5000")
print("4. bendera - RP.6000")

pdl = 15000
logo = 7000
lokasi = 5000
bendera = 6000

jumlah_pdl = int(input("jumlah beli pdl: "))
jumlah_logo = int(input("jumlah beli logo: "))
jumlah_lokasi = int(input("jumlah beli lokasi: "))
jumlah_bendera = int(input("jumlah beli bendera: "))

total_pdl = jumlah_pdl * pdl
total_logo = jumlah_logo * logo
total_lokasi = jumlah_lokasi * lokasi
total_bendera = jumlah_bendera * bendera

total_bayar = total_pdl + total_logo + total_lokasi + total_bendera

print("\n=== STRUK PEMBELIAN ===")
print("Pdl     : Rp.", total_pdl)
print("Logo    : Rp.", total_logo)
print("Lokasi  : Rp.", total_lokasi)
print("Bendera : Rp.", total_bendera)
print("------------------------------")
print("total belanja: Rp.", total_bayar)