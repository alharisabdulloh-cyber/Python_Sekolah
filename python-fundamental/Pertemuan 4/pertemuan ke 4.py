#latihan 1
# Cetak semua kelipatan 7 dari 0 sampai 70
for i in range(0, 71, 7):
    print(i)

#latihan 2
# Membalik string "Python"
kalimat = "Python"
kalimat_terbalik = ""

for huruf in kalimat:
    kalimat_terbalik = huruf + kalimat_terbalik

print(kalimat_terbalik)  # Output: nohtyP

#latihan 3
# Hitung angka yang habis dibagi 3 dan 5 dari 1 sampai 50
count = 0

for angka in range(1, 51):
    if angka % 3 == 0 and angka % 5 == 0:
        count += 1

print("Jumlah angka yang habis dibagi 3 dan 5:", count)

#latihan 4
# Pola segitiga terbalik
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

#latihan 5
# Hitung faktorial dengan for loop
n = int(input("Masukkan bilangan bulat positif: "))

hasil_faktorial = 1
for i in range(1, n + 1):
    hasil_faktorial *= i

print(f"Faktorial dari {n} adalah {hasil_faktorial}")
