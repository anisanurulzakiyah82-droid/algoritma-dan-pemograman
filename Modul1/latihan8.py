total = 0
for i in range(1, 6):
    nilai = float(input(f"Masukkan nilai ke-{i}: "))
    total += nilai

rata_rata = total / 5
print("rata-rata nilai:", rata_rata)