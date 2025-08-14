#Latihan 1: Fungsi dengan Argumen Default
def buat_email(nama_pengguna, domain="coding.com"):
    return f"{nama_pengguna.lower()}@{domain.lower()}"

# Contoh pemanggilan
print(buat_email("Budi"))          # budi@coding.com
print(buat_email("Ani", "belajar.id"))  # ani@belajar.id

#Latihan 2: Memanggil dengan Keyword Arguments
def kirim_paket(barang, tujuan, berat_kg, asuransi=False, express=False):
    print(f"Mengirim {barang} ke {tujuan}")
    print(f"Berat: {berat_kg} kg")
    print(f"Asuransi: {asuransi}")
    print(f"Express: {express}")

# Panggil dengan keyword arguments
kirim_paket(barang="Buku", tujuan="Bandung", berat_kg=2, express=True)

#Latihan 3: Mengembalikan Banyak Nilai
def analisis_daftar(daftar_angka):
    total = sum(daftar_angka)
    jumlah = len(daftar_angka)
    rata_rata = total / jumlah if jumlah > 0 else 0
    return total, jumlah, rata_rata

# Contoh pemanggilan
angka = [10, 20, 30, 40, 50]
total, jumlah, rata_rata = analisis_daftar(angka)
print("Total:", total)
print("Jumlah elemen:", jumlah)
print("Rata-rata:", rata_rata)

#Latihan 4: Dokumentasi Profesional (Docstring)
def analisis_daftar(daftar_angka):
    """
    Menganalisis sebuah daftar angka.

    Args:
        daftar_angka (list of int/float): Daftar angka yang ingin dianalisis.

    Returns:
        tuple: Berisi tiga nilai:
            - total (int/float): Jumlah total semua angka.
            - jumlah (int): Banyaknya elemen dalam daftar.
            - rata_rata (float): Nilai rata-rata dari semua angka.
    """
    total = sum(daftar_angka)
    jumlah = len(daftar_angka)
    rata_rata = total / jumlah if jumlah > 0 else 0
    return total, jumlah, rata_rata

# Cek docstring
help(analisis_daftar)

#Latihan 5: Konversi ke Lambda
# Fungsi biasa
def get_luas_lingkaran(radius):
    return 3.14159 * (radius ** 2)

# Versi lambda
luas_lingkaran_lambda = lambda radius: 3.14159 * (radius ** 2)

# Uji
print(get_luas_lingkaran(5))        # Fungsi biasa
print(luas_lingkaran_lambda(5))     # Fungsi lambda
