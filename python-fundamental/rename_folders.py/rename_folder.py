import os

# Dapatkan direktori kerja saat ini
root_folder = os.getcwd()

# Loop semua folder di root
for folder in os.listdir(root_folder):
    old_path = os.path.join(root_folder, folder)

    # Cek hanya folder dengan nama "Pertemuan x"
    if os.path.isdir(old_path) and folder.lower().startswith("pertemuan "):
        parts = folder.split(" ")
        if len(parts) == 2 and parts[1].isdigit():
            # Format ulang jadi 2 digit, misalnya "Pertemuan 01"
            new_name = f"Pertemuan {int(parts[1]):02}"
            new_path = os.path.join(root_folder, new_name)

            os.rename(old_path, new_path)
            print(f"Renamed: {folder} → {new_name}")

print("✅ Semua folder berhasil dirapikan!")

