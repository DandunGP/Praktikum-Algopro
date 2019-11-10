Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Dandun Gigih Prakoso'
>>> NIM = 'L200190172'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # variabel a merupakan data tipe integer karena telah diubah dari data tipe sting menjadi data tipe integer
>>> type(b)
<class 'int'>
>>> # variabel b merupakan data tipe integer karena data tersebut mengandung intruksi len yang mana len adalah jumlah anggota dari suatu objek
>>> a / b
58.6
>>> # merupakan data yang bertipe float karena 1172 dibagi 20 menghasilkan bilangan float 58.6 atau mengandung nilai desimal
>>> a // b
58
>>> # merupakan data yang bertipe integer karena hasil bagi dari 1172 dibagi 20 yang hasilnya 58.6 dibulat kan kebawah menjadi 58 yang bertipe integer, karena data bertipe integer dibagi data bertipe integer maka menghasilkan data bertipe integer pula
>>> 10 * (a - 999)
1730
>>> # merupakan data yang bertipe integer , karena data dari variabel a dikurang 999 adalah 173 dan kemudian dikalikan dengan 10 menghasilkan data 1730
>>> b ** 2
400
>>> # merupakan data yang bertipe integer , karena data dari variabel b pangkat kan 2 atau 20 pangkat 2 yang menghasilkan data 400
>>> a % b
12
>>> # merupakan data yang bertipe integer , karena simbol % merupakan sisa hasil bagi dari data variabel a dibagi data variabel b atau sisa hasil bagi dari 1172 dibagi 20 yaitu 12
>>> c = 12.5
>>> # data 12.5 disimpan dalam variabel c
>>> type(c)
<class 'float'>
>>> # variabel c merupakan data float karena mengandung nilai desimal
>>> a / c
93.76
>>> # merupakan data bertipe float karena data variabel a dibagi dengan data variabel c sama dengan 93.76 atau 1172 dibagi 12.5 menghasilkan data 93.76 yang bertipe float atau bernilai desimal
>>> a // c
93.0
>>> # merupakan data yang bertipe float karena dalam variabel c mengandung data bertipe float maka hasil pembagian dibulatkan kebawah dari variabel data bertipe integer dibagi variabel data bertipe float adalah data bertipe float (1172 dibagi 12.5 dan dibulatkan ke bawah menghasilkan data 93.0)
>>> a % c
9.5
>>> # merupakan data yang bertipe float karena sisa hasil bagi(%) antara data variabel a(1172) dengan data variabel c(12.5) menghasilkan 9.5 yang mengandung nilai desimal
>>> c > b
False
>>> # merupakan data yang bertipe boolean yang bernilai atau berkondisi False karena data variabel c (12.5) lebih kecil dari data variabel b (20) sedangkan dalam program ditulis data variabel c lebih besar dari pada data variabel b maka menghasilkan kondisi atau nilai False
>>> type(c > b)
<class 'bool'>
>>> # merupakan data yang bertipe boolean yang memiliki 2 kondisi atau nilai yaitu True dan False , merupakan operator logika
>>> a > b and b > c
True
>>> # merupakan data yang bertipe boolean yang berkondisi atau bernilai True karena a > b bernilai True dan b > c bernilai True juga , dalam operator 'and' apabila kedua data memiliki nilai True maka menghasilkan data bernilai True
>>> a > 1100 or b < 10
True
>>> # merupakan data yang bertipe boolean yang berkondisi atau bernilai True karena a > 1100 bernilai True dan b < 10 bernilai False , dalam operator 'or' apabila salah satu memiliki nilai True maka menghasilkan data bernilai True juga
>>> 
