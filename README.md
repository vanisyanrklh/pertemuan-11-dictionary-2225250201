"""# Pertemuan 11 - Dictionary/Map

**Nama:** Vanisya Nur Khalimah  
**NIM:** 2225250201
**Kelas:** 3B 

## Tujuan
1. Memodelkan data pendidikan menggunakan *dictionary* dan pasangan *key-value*.
2. Memahami penggunaan *nested dictionary* untuk mengelola data berstruktur.
3. Menerapkan fungsi modular untuk operasi pencarian, manipulasi data (tambah & perbarui), iterasi, dan perhitungan statistik nilai mahasiswa.
4. Menghindari kesalahan *KeyError* saat melakukan akses data pada *dictionary*.

## Struktur Data
Program ini memanfaatkan struktur data **Nested Dictionary** (dictionary bersarang) dengan ketentuan sebagai berikut:
* **Key Utama (Primary Key):** Menggunakan **NIM** (Tipe Data: `str`, Contoh: `"A001"`, `"A002"`).
* **Value:** Berupa *dictionary* yang menyimpan detail atribut mahasiswa:
  * `"nama"` (`str`): Nama lengkap mahasiswa.
  * `"kelas"` (`str`): Kelas mahasiswa (misal: `"A"` atau `"B"`).
  * `"nilai"` (`int`): Nilai hasil belajar mahasiswa.

```python
# Visualisasi Struktur Data
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78}
}
```

## Cara Menjalankan
1. Pastikan Python 3 sudah terinstal pada komputer Anda.
2. Buka terminal atau *command prompt*, lalu arahkan ke direktori proyek.
3. Jalankan perintah berikut:
```bash
python3 data_mahasiswa.py
```

## Test Case

| No | Input / Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `cari_mahasiswa(data_mahasiswa, "A003")` | Menampilkan detail data mahasiswa Citra | `{'nama': 'Citra', 'kelas': 'B', 'nilai': 92}` | **Lulus** |
| 2 | `cari_mahasiswa(data_mahasiswa, "A999")` | Menampilkan pesan alternatif tanpa mengalami *crash* | `"Data mahasiswa tidak ditemukan"` | **Lulus** |
| 3 | Tambah Data Baru (`"A006"`) | Data NIM `"A006"` (Fajar) berhasil ditambahkan | Data Fajar tercantum pada rekap akhir | **Lulus** |
| 4 | Pembaruan Nilai (`"A002"`) | Nilai Budi berubah dari 78 menjadi 82 | Nilai Budi pada rekap tercetak `82` | **Lulus** |
| 5 | Rekap Data (`.items()`) | Menampilkan seluruh pasangan NIM dan detail data | Seluruh baris data mahasiswa ditampilkan terstruktur | **Lulus** |
| 6 | `rata_rata_nilai(data_mahasiswa)` | Menghitung rata-rata nilai dari seluruh data mahasiswa | Menghitung rata-rata kelas dengan tepat (`83.50`) | **Lulus** |

## Refleksi
* **Kesalahan Akses Key:**
  Pada awal pengembangan, akses data dilakukan secara langsung menggunakan kurung siku, yaitu `data[nim]`. Ketika dilakukan uji coba pencarian untuk NIM yang belum terdaftar (misalnya `"A999"`), program langsung terhenti (*crash*) dan mengeluarkan *error* `KeyError: 'A999'`.
* **Cara Memperbaiki:**
  Masalah ini diatasi dengan memanfaatkan method bawaan dictionary yaitu **`.get(key, default_value)`**. Dengan mengganti sintaks menjadi `data.get(nim, "Data mahasiswa tidak ditemukan")`, program dapat secara aman mengembalikan pesan default jika *key* tidak ada tanpa menghentikan eksekusi program.
"""

def buat_file_readme():
    nama_file = "README.md"
    try:
        # Menulis isi_readme ke dalam berkas README.md
        with open(nama_file, "w", encoding="utf-8") as file:
            file.write(isi_readme)
        print(f"Berhasil! Berkas '{nama_file}' telah dibuat.")
    except Exception as e:
        print(f"Gagal membuat berkas README: {e}")

if __name__ == "__main__":
    buat_file_readme()