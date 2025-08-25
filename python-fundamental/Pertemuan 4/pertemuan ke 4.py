# ==========================
# Latihan 1: Program Perhitungan Upah dengan Lembur
# ==========================
print("=== Latihan 1: Perhitungan Upah ===")
jam = float(input("Masukkan jumlah jam kerja: "))
tarif = float(input("Masukkan tarif per jam: "))

if jam > 40:
    # 40 jam normal
    upah_normal = 40 * tarif
    # sisanya lembur
    lembur = (jam - 40) * tarif * 1.5
    total = upah_normal + lembur
else:
    total = jam * tarif

print("Pay:", total)
print()

# ==========================
# Latihan 2: Program Upah yang Aman dari Error
# ==========================
print("=== Latihan 2: Upah dengan Error Hand
