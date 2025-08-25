# proyek_kasir.py

print("============================================")
print(" SELAMAT DATANG DI PROGRAM KASIR CERDAS! ")
print("============================================")

# --- Input Barang 1 ---
print("\n--- Masukkan Detail Barang 1 ---")
nama_barang_1 = input("Nama Barang: ")
harga_1 = float(input("Harga Satuan: Rp 40.000.00"))
jumlah_1 = int(input("Jumlah: "))

# --- Input Barang 2 ---
print("\n--- Masukkan Detail Barang 2 ---")
nama_barang_2 = input("Nama Barang: ")
harga_2 = float(input("Harga Satuan: Rp "))
jumlah_2 = int(input("Jumlah: "))

print("\nMenghitung total...")

# --- Kalkulasi Total ---
total_1 = harga_1 * jumlah_1
total_2 = harga_2 * jumlah_2
subtotal = total_1 + total_2

# --- Logika Diskon ---
jumlah_diskon = 0.0
persen_diskon = 0

if subtotal > 200_000:
    persen_diskon = 10
    jumlah_diskon = subtotal * 0.10
elif subtotal > 100_000:
    persen_diskon = 5
    jumlah_diskon = subtotal * 0.05

total_akhir = subtotal - jumlah_diskon

# --- Cetak Struk ---
print("============================================")
print(" STRUK PEMBELIAN ANDA")
print("============================================")
print("Detail Belanja:")
print(f"1. {nama_barang_1} ({jumlah_1} x Rp {harga_1}) = Rp {total_1}")
print(f"2. {nama_barang_2} ({jumlah_2} x Rp {harga_2}) = Rp {total_2}")
print("--------------------------------------------")
print(f"Subtotal : Rp {subtotal}")
print(f"Diskon ({persen_diskon}%) : - Rp {jumlah_diskon}")
print("--------------------------------------------")
print(f"Total yang harus dibayar: Rp {total_akhir}")
print("============================================")
print(" TERIMA KASIH TELAH BERBELANJA! ")
print("============================================")

