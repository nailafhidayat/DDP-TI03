def duplicate(buah_buahan):
    hasilduplicate = []

# Menggunakan for
    for nama_buah in buah_buahan:
        hasilduplicate.append(nama_buah)
        hasilduplicate.append(nama_buah)
    return hasilduplicate

# Memanggil fungsi
buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
hasil = duplicate(buah)
print(hasil)