## Program Akun
## Dibuat oleh Dandun L200190172
import random
angka = random.randint(0,1000)

Nama = 'Dandun Gigih Prakoso'
TanggalLahir = '25 Juni 2001'
NamaSingkat = Nama[0] + '.' + Nama[7] + '.' + Nama[13:22]
Username = Nama[0] + TanggalLahir[0:2] + TanggalLahir[8:14]
Password = Nama[0:3] + str(angka)
