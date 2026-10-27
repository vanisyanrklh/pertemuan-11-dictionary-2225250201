def cari_mahasiswa(data, nim):
    # Menggunakan .get() agar jika NIM tidak ditemukan, mengembalikan pesan "Data tidak ditemukan"
    return data.get(nim, "Data tidak ditemukan")

def rata_rata_nilai(data):
    if not data:
        return 0
    total_nilai = sum(info["nilai"] for info in data.values())
    return total_nilai / len(data)

# Dictionary awal sesuai kerangka program
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

print("=== MENJALANKAN TEST CASE WAJIB ===\n")

# 1. Test Case: Pencarian tersedia (Input: A003)
print("1. Pencarian Tersedia (A003):")
print(cari_mahasiswa(data_mahasiswa, "A003"))
print()

# 2. Test Case: Pencarian tidak tersedia (Input: A999)
print("2. Pencarian Tidak Tersedia (A999):")
print(cari_mahasiswa(data_mahasiswa, "A999"))
print()

# 3. Test Case: Pembaruan nilai (Input: A002 menjadi 82)
print("3. Pembaruan Nilai A002:")
print("Nilai sebelum:", data_mahasiswa["A002"]["nilai"])
data_mahasiswa["A002"]["nilai"] = 82
print("Nilai setelah diperbarui:", data_mahasiswa["A002"])
print()

# 4. Test Case: Penambahan data (Input: A006)
print("4. Penambahan Data A006:")
data_mahasiswa["A006"] = {"nama": "Fajar", "kelas": "B", "nilai": 90}
print("Hasil pengecekan A006:", cari_mahasiswa(data_mahasiswa, "A006"))
print()

# 5. Test Case: Rekap (Input: items())
print("5. Rekap Menggunakan items():")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} | Nama: {info['nama']} | Kelas: {info['kelas']} | Nilai: {info['nilai']}")