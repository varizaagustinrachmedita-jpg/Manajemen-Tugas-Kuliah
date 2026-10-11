
from .processing import Tugas


def tes_tugas():
    # Mengecek apakah tugas bisa dibuat dengan benar
    tugas = Tugas(
        "Tugas Basis Data",
        "2026-10-20",
        "Tinggi"
    )

    assert tugas.judul == "Tugas Basis Data"
    assert tugas.prioritas == "Tinggi"
    assert tugas.status == "Belum selesai"

    print("Tes tugas berhasil.")


def tes_judul_kosong():
    # Judul kosong seharusnya menghasilkan error
    try:
        Tugas("", "2026-10-20")
    except ValueError:
        print("Tes judul kosong berhasil.")
    else:
        print("Tes judul kosong gagal.")


if __name__ == "__main__":
    tes_tugas()
    tes_judul_kosong()
