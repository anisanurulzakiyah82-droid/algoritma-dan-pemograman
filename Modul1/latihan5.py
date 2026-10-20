nilai = float(input("Masukkan nilai mahasiswa: "))

if 0 <= nilai <= 100:
    if nilai >= 60:
        print("Mahasiswa dinyatakan lulus")
    else:
        print("Mahasiswa dinyatakan tidak lulus")
else:
    print("Nilai tidakk valid")