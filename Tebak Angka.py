import random

minRange = 1
maxRange = 10
randomRange = random.randint(minRange, maxRange)

guess = int(input("Masukkan tebakan angka 1-10: "))

while guess != randomRange:
    if guess < randomRange:
        print("Angka Terlalu Rendah")
    else:
        print("Angka Terlalu Besar")
    guess = int(input("Coba lagi: "))

print("Selamat anda benar.")