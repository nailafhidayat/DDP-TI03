# info_gempa.py
from Gempa import Gempa

# Membuat objek gempa
gempa_pertama = Gempa("Banten", 1.2)
gempa_kedua = Gempa("Palu", 6.1)
gempa_ketiga = Gempa("Cianjur", 5.6)
gempa_keempat = Gempa("Jayapura", 3.3)
gempa_kelima = Gempa("Garut", 4.0)

# Menampilkan informasi dampak gempa
print("Gempa Pertama:", gempa_pertama.dampak())
print("Gempa Kedua:", gempa_kedua.dampak())
print("Gempa Ketiga:", gempa_ketiga.dampak())
print("Gempa Keempat:", gempa_keempat.dampak())
print("Gempa Kelima:", gempa_kelima.dampak())
