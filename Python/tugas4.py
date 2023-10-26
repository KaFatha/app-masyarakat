
k = ["B 1237 BOS","Supra X",300,"Merah"]
k.append("20 jt")
k.append("2")
k.insert(2,"Honda")
k.insert(3,"Motor")
print(k)


hitung = input("Menghitung Luas Bangun Datar : ")

match hitung:
    case "Persegi"|"persegi"|"PERSEGI":
        sisi = int(input("Masukkan sisi : "))
        hasil1 = sisi * sisi
        print(hasil1)
    case "Lingkaran"|"lingkaran"|"LINGKARAN":
        jari = int(input("Masukkan Jari-jari : "))
        hasil2 = 1/4* 22/7 * jari
        print(hasil2)
    case "Segitiga"|"segitiga"|"SEGITIGA":
        alas = int(input("Masukkan Alas : "))
        tinggi = int(input("Masukkan Tinggi : "))
        hasil3 = 0.5 * alas * tinggi
        print(hasil3)
    case _:
        print("Salah Memasukkan Pilihan")
