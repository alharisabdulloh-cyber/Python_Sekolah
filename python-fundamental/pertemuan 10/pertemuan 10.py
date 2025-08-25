import re   # dipakai untuk Latihan 5 (hapus karakter selain huruf/angka/-)

# ============================
# Latihan 1: Standarisasi Judul
# ============================
print("Latihan 1: Standarisasi Judul")
judul = input("Masukkan judul buku: ")
judul_bersih = judul.strip().title()
print("Judul standar:", judul_bersih)
print("-" * 40)


# ============================
# Latihan 2: Validasi Email Sederhana
# ============================
print("Latihan 2: Validasi Email")
email = input("Masukkan alamat email: ")

if "@" in email and (email.endswith(".com") or email.endswith(".co.id")):
    print("Email valid")
else:
    print("Email tidak valid")
print("-" * 40)


# ============================
# Latihan 3: Sensor Kata
# ============================
print("Latihan 3: Sensor Kata")
kalimat = input("Masukkan sebuah kalimat: ")
kata_sensor = input("Masukkan kata yang ingin disensor: ")
kalimat_sensored = kalimat.replace(kata_sensor, "***")
print("Hasil sensor:", kalimat_sensored)
print("-" * 40)


# ============================
# Latihan 4: Akronim Generator
# ============================
print("Latihan 4: Akronim Generator")
organisasi = input("Masukkan nama organisasi: ")
kata_kata = organisasi.split()
akronim = "".join([k[0].upper() for k in kata_kata])
print("Akronim:", akronim)
print("-" * 40)


# ============================
# Latihan 5: URL Slug Generator
# ============================
print("Latihan 5: URL Slug Generator")
judul_artikel = input("Masukkan judul artikel: ")
slug = judul_artikel.lower().strip()
slug = slug.replace(" ", "-")
# hapus karakter selain huruf, angka, dan tanda hubung
slug = re.sub(r'[^a-z0-9-]', '', slug)
print("Slug URL:", slug)
print("-" * 40)
