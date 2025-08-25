# ============================
# Latihan 1: Iterasi dan range()
# ============================
print("Latihan 1: Kelipatan 7 dari 0 sampai 70")
for i in range(0, 71, 7):   # mulai 0, berhenti di 70, langkah 7
    print(i)
print("-" * 30)


# ============================
# Latihan 2: Pola Akumulator dengan String
# ============================
print("Latihan 2: Membalik string 'Python'")
kalimat = "Python"
kalimat_terbalik = ""
for huruf in kalimat:
    kalimat_terbalik = huruf + kalimat_terbalik
print(kalimat_terbalik)   # Output: nohtyP
print("-" * 30)


# ============================
# Latihan 3: Pola Pencarian dengan if
# ============================
print("Latihan 3: Hitung angka 1–50 yang habis dibagi 3 dan 5")
count = 0
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        count += 1
print("Jumlah angka habis dibagi 3 dan 5:", count)
print("-" * 30)


# ============================
# Latihan 4: Nested Loops untuk Pola
# ============================
print("Latihan 4: Segitiga siku-siku terbalik")
for i in range(5, 0, -1):      # 5 sampai 1
    for j in range(i):
        print("*", end="")
    print()   # pindah baris
print("-" * 30)


# ============================
# Latihan 5: Faktorial
# ============================
print("Latihan 5: Faktorial")
n = int(input("Masukkan bilangan bulat positif: "))
hasil_faktorial = 1
for i in range(1, n + 1):
    hasil_faktorial *= i
print(f"Faktorial dari {n} adalah {hasil_faktorial}")
