
import unittest
from tugas_kuliah import Tugas, ManajemenTugas


class TesManajemenTugas(unittest.TestCase):

    def test_tambah_tugas(self):
        # Mengecek penambahan tugas
        data = ManajemenTugas()
        tugas = Tugas("Tugas Basis Data", "2026-10-20", "Tinggi")
        data.tambah_tugas(tugas)
        self.assertEqual(data.hitung_tugas(), 1)

    def test_judul_tugas(self):
        # Mengecek judul tugas
        tugas = Tugas("Tugas Python", "2026-10-22")
        self.assertEqual(tugas.judul, "Tugas Python")

    def test_prioritas_tugas(self):
        # Mengecek prioritas tugas
        tugas = Tugas("Tugas RPL", "2026-10-25", "Rendah")
        self.assertEqual(tugas.prioritas, "Rendah")

    def test_judul_kosong(self):
        # Judul kosong seharusnya ditolak
        with self.assertRaises(ValueError):
            Tugas("", "2026-10-20")

    def test_cari_tugas(self):
        # Mengecek pencarian berdasarkan judul
        data = ManajemenTugas()
        tugas = Tugas("Tugas Basis Data", "2026-10-20")
        data.tambah_tugas(tugas)
        hasil = data.cari_tugas("Basis")
        self.assertEqual(len(hasil), 1)

    def test_ubah_status(self):
        # Mengecek perubahan status
        data = ManajemenTugas()
        tugas = Tugas("Tugas Python", "2026-10-22")
        data.tambah_tugas(tugas)
        berhasil = data.ubah_status("Tugas Python", "Selesai")
        self.assertTrue(berhasil)
        self.assertEqual(tugas.status, "Selesai")


if __name__ == "__main__":
    unittest.main()
