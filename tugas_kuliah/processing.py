
from .validasi import cek_judul, cek_prioritas, cek_deadline


class Tugas:
    def __init__(self, judul, deadline, prioritas="Sedang", status="Belum selesai"):
        self.judul = cek_judul(judul)
        self.deadline = cek_deadline(deadline)
        self.prioritas = cek_prioritas(prioritas)
        self.status = status

    def tampilkan(self):
        # Menampilkan data tugas
        print("Judul     :", self.judul)
        print("Deadline  :", self.deadline)
        print("Prioritas :", self.prioritas)
        print("Status    :", self.status)


class ManajemenTugas:
    def __init__(self):
        self.daftar_tugas = []

    def tambah_tugas(self, *tugas):
        # Menambahkan satu atau beberapa tugas
        for item in tugas:
            self.daftar_tugas.append(item)

    def cari_tugas(self, kata_kunci):
        # Mencari tugas berdasarkan judul
        hasil = [
            tugas for tugas in self.daftar_tugas
            if kata_kunci.lower() in tugas.judul.lower()
        ]
        return hasil

    def urutkan_tugas(self):
        # Mengurutkan tugas berdasarkan deadline
        self.daftar_tugas.sort(key=lambda tugas: tugas.deadline)

    def ubah_status(self, judul, status="Selesai"):
        # Mengubah status tugas
        for tugas in self.daftar_tugas:
            if tugas.judul.lower() == judul.lower():
                tugas.status = status
                return True
        return False

    def hitung_tugas(self, *status):
        # Menghitung jumlah tugas sesuai status
        if not status:
            return len(self.daftar_tugas)

        return sum(
            1 for tugas in self.daftar_tugas
            if tugas.status in status
        )

    def buat_tugas(self, judul, **kwargs):
        # Membuat tugas dengan data tambahan
        deadline = kwargs.get("deadline", "")
        prioritas = kwargs.get("prioritas", "Sedang")
        status = kwargs.get("status", "Belum selesai")

        tugas = Tugas(
            judul=judul,
            deadline=deadline,
            prioritas=prioritas,
            status=status
        )
        self.tambah_tugas(tugas)
        return tugas


if __name__ == "__main__":
    # Tes singkat class dan fungsi
    data = ManajemenTugas()
    tugas_baru = Tugas("Tugas Basis Data", "2026-10-20", "Tinggi")
    data.tambah_tugas(tugas_baru)
    tugas_baru.tampilkan()
