#latihan 1
s = "Belajar Python itu Menyenangkan"

# Karakter pertama
print(s[0])     # B

# Karakter terakhir (pakai indexing negatif)
print(s[-1])    # n

# Karakter spasi pertama (di indeks 7)
print(s[7])     # " "

#latihan 2
s = "Belajar Python itu Menyenangkan"

# "Python"
print(s[8:14])

# "Menyenangkan"
print(s[18:])

# "Belajar"
print(s[:7])

#latihan 3
# Minta input kata dari user
kata = input("Masukkan sebuah kata: ")

# Membalik kata dengan slicing
kata_terbalik = kata[::-1]
print("Kata terbalik:", kata_terbalik)

# Cek apakah palindrom
if kata.lower().replace(" ", "") == kata_terbalik.lower().replace(" ", ""):
    print("Ini adalah palindrom!")
else:
    print("Bukan palindrom.")

#latihan 4
kalimat = "BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"

# Ambil setiap karakter ke-3
kode_rahasia = kalimat[::3]
print("Kode rahasia:", kode_rahasia)

#latihan 5
nama_salah = "dUDI sANTOSO"

# "dUDI" -> ambil "UDI" lalu jadi "udi", lalu ganti "d" jadi "B"
# "sANTOSO" -> ambil "ANTOSO" lalu jadi "antoso", lalu ganti "s" jadi "S"

nama_benar = "B" + nama_salah[1:3].lower() + "i" + " " + "S" + nama_salah[6:].lower()
print(nama_benar)   # Budi Santoso

