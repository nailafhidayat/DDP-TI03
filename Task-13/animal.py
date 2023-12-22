class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup 
        self.berkembang_biak = berkembang_biak
    
class Jerapah(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, ciri_khas, tinggi):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.ciri_khas = ciri_khas
        self.tinggi = tinggi

    def info(self):
        print("\n==========================")
        print("Jerapah \t:", self.name)
        print("Makanan \t:", self.makanan)
        print("Hidup \t\t:", self.hidup)
        print("Berkembang Biak :", self.berkembang_biak)
        print("Ciri Khas \t:", self.ciri_khas)
        print("Tinggi \t\t:", self.tinggi)
        print("\n--------------------------")

    def fun_fact(self):
        print("Jerapah tidur menggunakan bagian belakang lehernya sebagai bantalan.")

class Burung(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, Jenis, Warna):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis = Jenis
        self.warna = Warna

    def info(self):
        print("\n==========================")
        print("Burung \t\t:", self.name)
        print("Makanan \t:", self.makanan)
        print("Hidup \t\t:", self.hidup)
        print("Berkembang Biak :", self.berkembang_biak)
        print("Jenis \t\t:", self.jenis)
        print("Warna \t\t:", self.warna)
        print("\n--------------------------")

    def terbang(self):
        print("Burung Dara terbang dengan baik di udara.")

class Ikan(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, Tipe, Warna):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.tipe = Tipe
        self.warna = Warna

    def info(self):
        print("\n==========================")
        print("Ikan \t\t:", self.name)
        print("Makanan \t:", self.makanan)
        print("Hidup \t\t:", self.hidup)
        print("Berkembang Biak :", self.berkembang_biak)
        print("Tipe \t\t:", self.tipe)
        print("Warna \t\t:", self.warna)
        print("\n--------------------------")

    def berenang(self):
        print("Ikan Koi masih merupakan keluarga serumpun dari ikan Mas.")

jerapah1 = Jerapah("Jerapah Somalia", "Tumbuhan", "Darat", "Vivipar", "Leher Panjang", "5 Meter")
jerapah1.info()
jerapah1.fun_fact()

burung1 = Burung("Burung Dara", "Biji - bijian", "Udara", "Ovipar", "Aves", "Putih")
burung1.info()
burung1.terbang()

ikan1 = Ikan("Ikan Koi", "Pelet", "Air", "Ovipar", "Ikan Hias", "Merah")
ikan1.info()
ikan1.berenang()
