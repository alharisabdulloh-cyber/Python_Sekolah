# ============================
# Latihan 1: Tampilkan Semua Uppercase
# ============================

print("Latihan 1: Tampilkan Semua Uppercase")
nama_file = input("Masukkan nama file (misal: puisi.txt): ")

try:
    with open(nama_file, "r", encoding="utf-8") as f:
        for baris in f:
            print(baris.strip().upper())
except FileNotFoundError:
    print("File tidak ditemukan!")
print("-" * 50)


# ============================
# Latihan 2: Hitung Rata-rata Spam Confidence
# ============================

print("Latihan 2: Hitung Rata-rata Spam Confidence")
nama_file = input("Masukkan nama file (misal: mbox-short.txt): ")

try:
    total = 0
    count = 0
    with open(nama_file, "r", encoding="utf-8") as f:
        for baris in f:
            if baris.startswith("X-DSPAM-Confidence:"):
                # ambil angka setelah titik dua
                nilai = float(baris.split(":")[1].strip())
                total += nilai
                count += 1
    if count > 0:
        print("Rata-rata spam confidence:", total / count)
    else:
        print("Tidak ada baris X-DSPAM-Confidence ditemukan.")
except FileNotFoundError:
    print("File tidak ditemukan!")
print("-" * 50)


# ============================
# Latihan 3: Easter Egg File
# ============================

print("Latihan 3: Easter Egg File")
nama_file = input("Masukkan nama file: ")

if nama_file == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            for baris in f:
                print(baris.strip())
    except FileNotFoundError:
        print("File tidak ditemukan!")
