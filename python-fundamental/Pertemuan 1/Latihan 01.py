# Latihan 1: Perbedaan ekspresi unar dan biner
print("=== Latihan 1 ===")
x = -5    # ekspresi unar
y = not True   # ekspresi unar
z = 7 + 3      # ekspresi biner
k = 10 > 5     # ekspresi biner
print(f"Unary contoh: x = {x}, y = {y}")
print(f"Binary contoh: z = {z}, k = {k}\n")

# Latihan 2: Tipe data ekspresi relasional
print("=== Latihan 2 ===")
relasi = (10 > 5)
print(f"10 > 5 = {relasi}, tipe data: {type(relasi)}\n")

# Latihan 3: Prediksi output
print("=== Latihan 3 ===")
hasil = (5 + 2) * 3 - (8 / 4)
print(f"(5 + 2) * 3 - (8 / 4) = {hasil}\n")

# Latihan 4: Perbandingan string
print("=== Latihan 4 ===")
print(f'"Apple" < "Banana" = {"Apple" < "Banana"}\n')

# Latihan 5: Kesalahan operator +=
print("=== Latihan 5 ===")
poin = 100
# poin =+ 50   # salah
poin += 50     # benar
print(f"Hasil poin setelah ditambah 50 = {poin}\n")

# Latihan 6: Hitung total detik dalam 1 hari
print("=== Latihan 6 ===")
detik = 24 * 60 * 60
print(f"Total detik dalam 1 hari = {detik}\n")

# Latihan 7: Program input nama dan tahun lahir
print("=== Latihan 7 ===")
nama = input("Masukkan nama: ")
tahun_lahir = int(input("Masukkan tahun lahir: "))
umur = 2025 - tahun_lahir
print(f"Halo {nama}, di tahun 2025 umur kamu sekitar {umur} tahun.")
