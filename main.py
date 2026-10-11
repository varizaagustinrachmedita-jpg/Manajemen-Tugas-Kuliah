from tugas_kuliah import Tugas, ManajemenTugas
from tugas_kuliah.fileio import (
    simpan_tugas,
    simpan_semua_tugas,
    baca_tugas,
    simpan_laporan,
)
from tugas_kuliah.validasi import cek_status


def tampilkan_menu():
    # Menampilkan pilihan menu
    print("\n=== MANAJEMEN TUGAS KULIAH ===")
    print("1. Tambah tugas")
    print("2. Lihat semua tugas")
    print("3. Cari tugas")
    print("4. Urutkan tugas")
    print("5. Ubah status tugas")
    print("6. Lihat jumlah tugas")
    print("7. Buat laporan")
    print("0. Keluar")


def simpan_semua(manajemen):
    # Menyimpan semua tugas menggunakan fungsi dari fileio
    simpan_semua_tugas(manajemen.daftar_tugas)


def muat_data():
    # Membaca data yang sudah tersimpan
    manajemen = ManajemenTugas()

    for data in baca_tugas():
        try:
            tugas = Tugas(
                judul=data[0],
                deadline=data[1],
                prioritas=data[2],
                status=data[3]
            )
            manajemen.tambah_tugas(tugas)
        except (ValueError, IndexError):
            print("Data tidak valid, jadi dilewati.")

    return manajemen




def tambah_tugas(manajemen):
    # Meminta data tugas baru dan menyimpannya
    try:
        judul = input("Judul tugas: ")
        deadline = input("Deadline (YYYY-MM-DD): ")
        prioritas = input("Prioritas (Rendah/Sedang/Tinggi): ")

        tugas = Tugas(
            judul=judul,
            deadline=deadline,
            prioritas=prioritas
        )

        manajemen.tambah_tugas(tugas)
        simpan_tugas(tugas)

    except ValueError as error:
        print("Data salah:", error)


        manajemen.tambah_tugas(tugas)
        simpan_tugas(tugas)

    except ValueError as error:
        print("Data salah:", error)


        manajemen.tambah_tugas(tugas)
        simpan_tugas(tugas)

    except ValueError as error:
        print("Data salah:", error)


def lihat_tugas(manajemen):
    # Menampilkan daftar tugas
    if not manajemen.daftar_tugas:
        print("Belum ada tugas.")
        return

    for nomor, tugas in enumerate(manajemen.daftar_tugas, start=1):
        print(f"\nTugas ke-{nomor}")
        tugas.tampilkan()


def cari_tugas(manajemen):
    # Mencari tugas berdasarkan judul
    kata = input("Masukkan judul yang dicari: ")
    hasil = manajemen.cari_tugas(kata)

    if hasil:
        for tugas in hasil:
            tugas.tampilkan()
    else:
        print("Tugas tidak ditemukan.")



def ubah_status(manajemen):
    # Memvalidasi dan mengubah status tugas
    judul = input("Judul tugas: ")
    status = input("Status baru (Belum selesai/Selesai): ")

    try:
        status = cek_status(status)
    except ValueError as error:
        print("Data salah:", error)
        return

    if manajemen.ubah_status(judul, status):
        simpan_semua(manajemen)
        print("Status berhasil diubah.")
    else:
        print("Tugas tidak ditemukan.")



def urutkan_tugas(manajemen):
    # Mengurutkan dan menyimpan kembali tugas
    manajemen.urutkan_tugas()
    simpan_semua(manajemen)
    lihat_tugas(manajemen)


def buat_laporan(manajemen):
    # Membuat laporan jumlah tugas
    jumlah = manajemen.hitung_tugas()
    selesai = manajemen.hitung_tugas("Selesai")
    belum = manajemen.hitung_tugas("Belum selesai")

    teks = (
        "LAPORAN MANAJEMEN TUGAS KULIAH\n"
        f"Total tugas: {jumlah}\n"
        f"Tugas selesai: {selesai}\n"
        f"Belum selesai: {belum}\n"
    )

    simpan_laporan(teks)
    print(teks)


def main():
    # Menjalankan program
    manajemen = muat_data()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_tugas(manajemen)
        elif pilihan == "2":
            lihat_tugas(manajemen)
        elif pilihan == "3":
            cari_tugas(manajemen)
        elif pilihan == "4":
            urutkan_tugas(manajemen)
        elif pilihan == "5":
            ubah_status(manajemen)
        elif pilihan == "6":
            print("Jumlah tugas:", manajemen.hitung_tugas())
        elif pilihan == "7":
            buat_laporan(manajemen)
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak tersedia.")


if __name__ == "__main__":
    main()
