#latihan 1
# Countdown dari 10 ke 1
hitung = 10

while hitung > 0:
    print(hitung)
    hitung -= 1

print("Blastoff!")

#latihan 2
# Game Tebak Angka
angka_rahasia = 7

while True:
    tebakan = int(input("Tebak angka (1-10): "))

    if tebakan == angka_rahasia:
        print("Selamat, tebakan Anda benar!")
        break
    else:
        print("Salah, coba lagi!")

print("Terima kasih sudah bermain!")

#latihan 3
# Input Angka Cerdas
total = 0
count = 0

while True:
    data = input("Masukkan angka (atau ketik 'done' untuk selesai): ")

    if data.lower() == "done":
        break

    try:
        angka = float(data)  # bisa menerima bilangan desimal juga
        total += angka
        count += 1
    except:
        print("Input tidak valid")
        continue

if count > 0:
    rata_rata = total / count
    print("Total:", total)
    print("Jumlah angka:", count)
    print("Rata-rata:", rata_rata)
else:
    print("Tidak ada angka yang dimasukkan.")


