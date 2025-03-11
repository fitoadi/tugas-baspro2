nama = str(input("Nama: "))
nik = int(input("NIK: "))
status = str(input ("Status (Pegawai Tetap/Honor): "))
gol = str(input("Golongan (A/B/C): "))

gaji = 0
bonus = 0

if(status == "Pegawai Tetap"):
    gaji = 1000000
    if gol == "A":
        bonus = 200000
    elif gol == "B":
        bonus = 400000
    elif gol == "C":
        bonus = 550000
    else:
        print("Golongan tidak valid!")
elif status == "Honor":
    gaji = 750000
    if gol == "A":
        bonus = 150000
    elif gol == "B":
        bonus = 275000
    elif gol == "C":
        bonus = 480000
    else:
        print("Golongan tidak valid!")
else:
    print("Status tidak valid!")

total_gaji = gaji + bonus

print("========= GAJI TOTAL =========")
print("Nama       :", nama)
print("NIK        :", nik)
print("Status     :", status)
print("Golongan   :", gol)
print("Gaji       : Rp.", gaji)
print("Bonus      : Rp.", bonus)
print("Gaji Total : Rp.", total_gaji)