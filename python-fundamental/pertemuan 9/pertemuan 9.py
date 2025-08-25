# ============================
# Latihan 1: Ahli Indexing
# ============================
s = "Belajar Python itu Menyenangkan"
print("Latihan 1:")
print("Karakter pertama:", s[0])       # B
print("Karakter terakhir:", s[-1])     # n
print("Karakter spasi pertama:", s[7]) # spasi
print("-" * 30)


# ============================
# Latihan 2: Master Slicing
# ============================
print("Latihan 2:")
print("Substring 'Python':", s[8:14])         # Python
print("Substring 'Menyenangkan':", s[18:])    # Menyenangkan
print("Substring 'Belajar':", s[:7])          # Belajar
print("-" * 30)


# ============================
# Latihan 3: Membalik Kata & Palindrom
# ============================
print("Latihan 3:")
kata = input("Masukkan sebuah kata: ")
kata_terbalik = kata[::-1]   # slicing dengan step -1
print("Kata terbalik:", kata_terbalik)

if kata.lower().replace(" ", "") == kata_terbalik.lower().replace(" ", ""):
    print("Ini adalah palindrom!")
else:
    print("Ini bukan palindrom.")
print("-" * 30)


# ============================
# Latihan 4: Kode Rahasia
# ============================
print("Latihan 4:")
kalimat = "BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"
kode_rahasia = kalimat[::3]   # ambil tiap karakter ke-3
print("Kode rahasia:", kode_rahasia)
print("-" * 30)


# ============================
# Latihan 5: Memperbaiki Nama
# ============================
print("Latihan 5:")
nama_salah = "dUDI sANTOSO"

# Ambil huruf pertama 'd' -> ubah jadi 'B'
huruf_depan = "B"

# Ambil 'UDI' -> ganti jadi 'udi'
belakang_depan = "udi"

# Ambil 's' -> ubah jadi 'S'
spasi = " "
huruf_s = "S"

# Ambil 'ANTOSO' -> ubah jadi 'antoso'
belakang_nama = "antoso"

nama_benar = huruf_depan + belakang_depan + spasi + huruf_s + belakang_nama
print("Nama diperbaiki:", nama_benar)   # Budi Santoso
