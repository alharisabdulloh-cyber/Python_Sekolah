# Latihan 1: Perbedaan utama antara operator = dan ==
# =  : assignment (memberi nilai ke variabel)
# == : comparison (membandingkan kesetaraan dua nilai)
print("Latihan 1:")
x = 5      # menggunakan '=' untuk memberi nilai
print("Nilai x =", x)
print("Apakah x == 5?", x == 5)  # menggunakan '==' untuk membandingkan
print()

# Latihan 2: Nama variabel yang TIDAK VALID
# a) _nama_depan  -> valid
# b) nilai_rata2  -> valid
# c) 2x           -> TIDAK VALID (tidak boleh diawali angka)
# d) namaLengkap  -> valid
print("Latihan 2:")
print("Jawaban: c) 2x (tidak valid karena nama variabel tidak boleh diawali angka)")
print()

# Latihan 3: Prediksi output kode
# angka_favorit = input("Masukkan angka favoritmu: ")
# hasil = angka_favorit * 2
# print(hasil)
# Jika input = 10 (string), maka hasil = "10" * 2 -> "1010"
print("Latihan 3:")
print("Jika input = 10, maka output =", "10" * 2)
print("Jawaban yang benar: b) Program akan menampilkan 1010")
print()

# Latihan 4: Program menghitung luas segitiga
print("Latihan 4:")
# Meminta pengguna memasukkan alas segitiga
alas = float(input("Masukkan alas segitiga: "))
# Meminta pengguna memasukkan tinggi segitiga
tinggi = float(input("Masukkan tinggi segitiga: "))
# Menghitung luas segitiga dengan rumus 0.5 * alas * tinggi
luas = 0.5 * alas * tinggi
# Menampilkan hasil ke layar
print(f"Luas segitiga adalah {luas}")
