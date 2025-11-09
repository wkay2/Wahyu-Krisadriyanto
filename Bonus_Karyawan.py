# Wahyu-Krisadriyanto
“Quiz OOP menghitung bonus karyawan”.

class Karyawan:
    def _init_(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def hitung_bonus(self):
        pass  # Method ini akan di-override oleh anak kelas


class KaryawanTetap(Karyawan):
    def hitung_bonus(self):
        return 0.10 * self.gaji


class KaryawanKontrak(Karyawan):
    def hitung_bonus(self):
        return 0.05 * self.gaji


# Membuat objek karyawan
budi = KaryawanTetap("Budi", 8000000)
sita = KaryawanKontrak("Sita", 6000000)

# Hitung total bonus
total_bonus = budi.hitung_bonus() + sita.hitung_bonus()

# Output bonus
print(f"Bonus Budi        : Rp{budi.hitung_bonus():,.0f}")
print(f"Bonus Sita        : Rp{sita.hitung_bonus():,.0f}")
print(f"Total Bonus Semua : Rp{total_bonus:,.0f}")