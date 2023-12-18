class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            return f"Gempa di {self.lokasi} tidak terasa."
        elif 2 <= self.skala < 4:
            return f"Gempa di {self.lokasi} menyebabkan retak-retak pada bangunan."
        elif 4 <= self.skala < 6:
            return f"Gempa di {self.lokasi} menyebabkan beberapa bangunan roboh."
        else:
            return f"Gempa di {self.lokasi} menyebabkan banyak bangunan roboh dan berpotensi tsunami."
