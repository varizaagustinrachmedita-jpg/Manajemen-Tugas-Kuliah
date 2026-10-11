
import os

# Lokasi folder utama proyek
FOLDER_PROYEK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAMA_FILE = os.path.join(FOLDER_PROYEK, "data_tugas.txt")


def buat_file():
    # Membuat file data jika belum ada
    try:
        with open(NAMA_FILE, "x", encoding="utf-8") as file:
            file.write("")
    except FileExistsError:
        pass
    except OSError as error:
        print("File tidak bisa dibuat:", error)


def simpan_tugas(tugas):
    # Menambahkan tugas baru ke file
    buat_file()

    try:
        with open(NAMA_FILE, "a", encoding="utf-8") as file:
            file.write(
                f"{tugas.judul}|{tugas.deadline}|"
                f"{tugas.prioritas}|{tugas.status}\n"
            )
        print("Data tugas berhasil disimpan.")
    except OSError as error:
        print("Data gagal disimpan:", error)


def baca_tugas():
    # Membaca semua data tugas dari file
    buat_file()
    daftar = []

    try:
        with open(NAMA_FILE, "r", encoding="utf-8") as file:
            for baris in file:
                data = baris.strip().split("|")

                if len(data) != 4:
                    print("Ada data rusak, baris dilewati.")
                    continue

                daftar.append(data)

    except FileNotFoundError:
        print("File data tugas tidak ditemukan.")

    return daftar


def simpan_laporan(teks):
    # Menyimpan laporan ke folder utama
    nama_laporan = os.path.join(FOLDER_PROYEK, "laporan_tugas.txt")

    try:
        with open(nama_laporan, "w", encoding="utf-8") as file:
            file.write(teks)
        print("Laporan berhasil disimpan.")
    except OSError as error:
        print("Laporan gagal disimpan:", error)


if __name__ == "__main__":
    buat_file()
    print("Lokasi file:", NAMA_FILE)
    print("Isi data:", baca_tugas())
