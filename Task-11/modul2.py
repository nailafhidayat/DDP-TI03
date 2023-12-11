# aritmatika.py

def tambah(a, b):
    hasil = a + b
    print("Fungsi untuk penjumlahan: ",hasil)

def kurang(a, b):
    hasil = a - b
    print ("Fungsi untuk pengurangan: ",hasil)

def kali(a, b):
    hasil = a * b
    print ("Fungsi untuk perkalian: ",hasil)

def bagi(a, b):
    if b == 0:
        print ("Tidak bisa dibagi dengan nol!")
    else:
        hasil = a / b
        print ("Fungsi untuk pembagian: ",hasil)

def pembagian_bulat(a, b):
    hasil = a // b
    print ("Fungsi untuk pembagian bulat: ",hasil)

def pangkat(a, b):
    hasil = a ** b
    print ("Fungsi untuk perpangkatan: ",hasil)

def modulus(a, b):
    hasil = a % b
    print ("Fungsi untuk modulus: ",hasil)

def operasi_campuran(a, b, c, d, e):
    hasil = (a + b) * c - d / e
    print ("Fungsi untuk operasi campuran: ",hasil)

def akar_kuadrat(a):
    if a >= 0:
        hasil = a ** 0.5
        print ("Fungsi untuk akar kuadrat: ",hasil)
    else:
        print ("Akar kuadrat dari bilangan negatif tidak didefinisikan")

def pangkat_empat(a):
    hasil = a ** 4
    print ("Fungsi untuk pangkat empat: ",hasil)