# ==========================
# Latihan 1: Fungsi Sapaan Sederhana
# ==========================
def salam_pembuka():
    print("==============================")
    print("Selamat Datang di Program Saya!")
    print("==============================")

# Panggil fungsi beberapa kali
salam_pembuka()
salam_pembuka()
print()  # baris kosong


# ==========================
# Latihan 2: Fungsi dengan Parameter
# ==========================
def info_cuaca(kota, cuaca):
    print(f"Cuaca di kota {kota} hari ini {cuaca}.")

# Contoh pemanggilan
info_cuaca("Jakarta", "berawan")
info_cuaca("Bandung", "hujan")
print()


# ==========================
# Latihan 3: Fungsi dengan return
# ==========================
def kubik(angka):
    return angka ** 3

hasil_kubik = kubik(4)
print("Hasil kubik dari 4 adalah:", hasil_kubik)
print()


# ==========================
# Latihan 4: Kalkulator Diskon
# =====
