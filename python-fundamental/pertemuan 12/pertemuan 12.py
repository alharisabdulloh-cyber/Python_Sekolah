import os

# ==========================
# Latihan 1: Membuat Log Sederhana
# ==========================
def buat_log():
    kegiatan = input("Masukkan kegiatan yang baru saja Anda lakukan: ")
    with open("log_kegiatan.txt", "a", encoding="utf-8") as file:
        file.write(kegiatan + "\n")
    print("Kegiatan berhasil dicatat di log_kegiatan.txt")


# ==========================
# Latihan 2: Salin File
# ==========================
def salin_file():
    try:
        with open("sumber.txt", "r", encoding="utf-8") as sumber:
            isi = sumber.read()
        with open("salinan.txt", "w", encoding="utf-8") as tujuan:
            tujuan.write(isi)
        print("Isi file berhasil disalin ke salinan.txt")
    except FileNotFoundError:
        print("File sumber.txt tidak ditemukan. Buat file terlebih dahulu.")


# ==========================
# Latihan 3: Hapus File dengan Aman
# ==========================
def hapus_file():
    nama_file = input("Masukkan nama file yang ingin dihapus: ")
    if os.path.exists(nama_file):
        konfirmasi = input(f"Anda yakin ingin menghapus {nama_file}? (y/n): ")
        if konfirmasi.lower() == "y":
            os.remove(nama_file)
            print(f"File {nama_file} berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print("File tidak ditemukan.")


# ==========================
# Program Utama (Menu)
# ==========================
while True:
    print("\n=== MENU PROGRAM ===")
    print("1. Tambah Log Kegiatan")
    print("2. Salin File (sumber.txt → salinan.txt)")
    print("3. Hapus File dengan Aman")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "1":
        buat_log()
    elif pilihan == "2":
        salin_file()
    elif pilihan == "3":
        hapus_file()
    elif pilihan == "4":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")

