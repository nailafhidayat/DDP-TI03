def balikan(buah_buahan):
    daftar_buah = len(buah_buahan)
    hasil_balikan = []

# Looping list menggunakan for
    for i in range(daftar_buah - 1, -1, -1):
        hasil_balikan.append(buah_buahan[i])

    return hasil_balikan

# Memanggil fungsi
buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
hasil = balikan(buah)
print(hasil)
