
def cek_judul(judul):
    # Judul tugas harus diisi
    if judul.strip() == "":
        raise ValueError("Judul tidak boleh kosong")
    return judul.strip()


def cek_prioritas(prioritas):
    # Pilihan prioritas tugas
    if prioritas not in ["Rendah", "Sedang", "Tinggi"]:
        raise ValueError("Prioritas tidak sesuai")
    return prioritas


def cek_deadline(deadline):
    # Deadline tidak boleh kosong
    if deadline.strip() == "":
        raise ValueError("Deadline harus diisi")
    return deadline.strip()


if __name__ == "__main__":
    print(cek_judul("Tugas Basis Data"))
    print(cek_prioritas("Tinggi"))
    print(cek_deadline("2026-10-20"))

def cek_status(status):
    # Memastikan status tugas sesuai pilihan
    if status not in ["Belum selesai", "Selesai"]:
        raise ValueError("Status tidak sesuai")
    return status
