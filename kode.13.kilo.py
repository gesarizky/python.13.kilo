# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput Jarak dalam Satuan Kilometer
kilometer = float(input("Tuliskan Jarak dalam Kilometer: "))

# Nilai Faktor Konversi
faktor_konversi = 1000

# Menghitung Jarak dalam Satuan Mil
m = kilometer * faktor_konversi

# Menampilkan Hasil Konversi Jarak
print('%0.2f Kilometer sama dengan %0.2f Meter' %(kilometer,m))
