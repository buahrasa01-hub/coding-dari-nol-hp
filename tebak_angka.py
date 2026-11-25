# Tebak Angka — latihan 2 dari tutorial "Coding dari Nol di HP"
# Channel YouTube Bu Ah (@buah2891)
# Cara menjalankan: python3 tebak_angka.py
# Komputer memilih angka acak 1 sampai 10, kalian harus menebaknya.
# Program memberi petunjuk "Terlalu kecil" atau "Terlalu besar".
# Tantangan: batasi jadi 5 tebakan saja, tampilkan sisa tebakan tiap giliran.

import random

rahasia = random.randint(1, 10)
tebakan = 0

while tebakan != rahasia:
    tebakan = int(input("Tebak angka 1 sampai 10: "))
    if tebakan < rahasia:
        print("Terlalu kecil")
    elif tebakan > rahasia:
        print("Terlalu besar")

print("Benar!")
