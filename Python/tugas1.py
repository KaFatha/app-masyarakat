a = "Fatahillah Kholiurahman"
b = "0110223273"
c = "TI09"
d = "085693781705"
e = '''Mampang Prapatan Jakarta Selatan'''

A = "Muhammmad iqbal"
B = "0110223280"
C = "TI09"
D = "085172449495"
E = "Bogor kemang residence"


print("Soal nomor 1")
print ("masukkan nama = "+a)
print ("masukkan Nim = "+b)
print ("masukkan Kelas = "+c)
print ("masukkan No Telpon = "+d)
print ("masukkan Alamat = "+e)

print ("  ")
print("Soal nomor 2")
print ("masukkan nama = "+A)
print ("masukkan Nim = "+B)
print ("masukkan Kelas = "+C)
print ("masukkan No Telpon = "+D)
print ("masukkan Alamat = "+E)

print("   ")
print("Soal nomor 3")
berat_badan = float(input("masukkan berat badan anda (kg) : "))
tinggi_badan = float(input("masukkan tinggi badan anda (cm) : "))

bmi = berat_badan/ (tinggi_badan * tinggi_badan)
if bmi < 18.5:
    print ("berat badan anda kurang dari standar")
elif 18.5 <= bmi < 24.9:
    print("berat badan anda normal")
elif 25.0 <= bmi < 29.9:
    print("berat badan anda over")
else:
    print("berat badan anda ideal")

print("   ")
print("Soal nomor 4")
celcius = float(input("Masukkan nilai celcius : "))
farenheit = (9/5)*celcius + 32
print("nilai dalam farenheit : ", farenheit, "f")

print("   ")
print("Soal nomor 5")
phi = 3.14
r = float(input("Masukkan panjang jari-jari tabung: "))
t = float(input("Masukkan panjang tinggi tabung: "))
rumus_luas = 2 * phi * r**2 + 2 * phi * r * t 
rumus_keliling = 2 * phi * r + 2 * phi * t

print("Luas Tabung", rumus_luas, "cm2", "dan Keliling", rumus_keliling, "cm2")





