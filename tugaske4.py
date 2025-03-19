# Input dari user
nama = input("Masukkan nama Anda: ")
nik = input("Masukkan NIK Anda: ")
status = input("Masukkan status Anda (Tetap/Honor): ").strip().lower()
gol = input("Masukkan golongan Anda (A/B/C): ").strip().upper()

# Data gaji pokok dan bonus berdasarkan status & golongan
liststatus = {"honor": 750000, "tetap": 1000000}
listbonus = {
    "honor": {"A": 150000, "B": 275000, "C": 480000},
    "tetap": {"A": 200000, "B": 400000, "C": 550000}
}

# Mencari gaji dan bonus yang sesuai
gajinya = 0
bonus = 0

for key in liststatus:
    if status == key:
        for gol_key in listbonus[key]:
            if gol == gol_key:
                gajinya = liststatus[key]
                bonus = listbonus[key][gol_key]
                break
        break

# Validasi input
gajitotal = gajinya + bonus
if gajinya == 0 and bonus == 0:
    print("Input status atau golongan tidak valid!")
else:
    # Cetak hasil
    print("\n==== Detail Gaji ====")
    print("Nama       :", nama)
    print("NIK        :", nik)
    print("Status     :", status.capitalize())
    print("Golongan   :", gol)
    print("Gaji       : Rp.", gajinya)
    print("Bonus      : Rp.", bonus)
    print("Total Gaji : Rp.", gajitotal)