# Latihan 1: Standarisasi Judul
judul = input("Masukkan judul buku: ")
judul_bersih = judul.strip().title()  # hilangkan spasi depan/belakang + ubah ke Title Case
print("Judul standar:", judul_bersih)


# Latihan 2: Validasi Email Sederhana
email = input("\nMasukkan alamat email: ")
if "@" in email and (email.endswith(".com") or email.endswith(".co.id")):
    print("Email valid")
else:
    print("Email tidak valid")


# Latihan 3: Sensor Kata
kalimat = input("\nMasukkan sebuah kalimat: ")
kata_sensor = input("Masukkan kata yang ingin disensor: ")
kalimat_sensor = kalimat.replace(kata_sensor, "***")
print("Kalimat setelah disensor:", kalimat_sensor)


# Latihan 4: Akronim Generator
organisasi = input("\nMasukkan nama organisasi: ")
kata_kata = organisasi.split()
akronim = "".join([kata[0].upper() for kata in kata_kata])
print("Akronim:", akronim)


# Latihan 5: URL Slug Generator
import re

judul_artikel = input("\nMasukkan judul artikel: ")
slug = judul_artikel.lower()          # ubah ke huruf kecil
slug = slug.strip()
slug = slug.replace(" ", "-")         # ganti spasi dengan -
slug = re.sub(r'[^a-z0-9\-]', '', slug)  # hapus karakter selain huruf, angka, dan -
print("Slug:", slug)
