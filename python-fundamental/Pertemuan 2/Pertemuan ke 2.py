Latihan 1

Ekspresi unar → hanya melibatkan satu operand (contoh: tanda negatif, not).
Ekspresi biner → melibatkan dua operand (contoh: +, -, *, /).

# Ekspresi unar
x = -5       # unary minus
y = not True # unary not

# Ekspresi biner
z = 7 + 3    # penjumlahan
k = 10 > 5   # perbandingan
print(x, y, z, k)

Latihan 2

Ekspresi relasional menghasilkan boolean (True atau False).

print(10 > 5)          # True
print(type(10 > 5))    # <class 'bool'>

Latihan 3

Kode:

print((5 + 2) * 3 - (8 / 4))


Urutan operasi (prioritas):

(5 + 2) = 7

(8 / 4) = 2.0

7 * 3 = 21

21 - 2.0 = 19.0

👉 Output = 19.0

Latihan 4
print("Apple" < "Banana")


Hasilnya True, karena perbandingan string dilakukan secara leksikografis (urutan alfabet).
Huruf "A" datang sebelum "B", jadi "Apple" < "Banana" bernilai True.

Latihan 5

Kode salah:

poin = 100
poin =+ 50   # ini artinya poin = +50, bukan menambah 50
print(poin)  # hasilnya 50


Seharusnya:

poin = 100
poin += 50   # shorthand untuk poin = poin + 50
print(poin)  # hasilnya 150

Latihan 6

Hitung total detik dalam satu hari:

print(24 * 60 * 60)  # 86400

Latihan 7

Minta input nama dan tahun lahir, lalu hitung umur di 2025:

nama = input("Masukkan nama: ")
tahun_lahir = int(input("Masukkan tahun lahir: "))
umur = 2025 - tahun_lahir
print(f"Halo {nama}, di tahun 2025 umur kamu sekitar {umur} tahun.")
