class Gempa: 
    # konstraktor Inisialisasi atribut
     def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    # Method Penentuan Skala Gempa
     def dampak(self):
        #Logika/Statmeant
        if self.skala < 2:
            print('Gempa Tidak Berasa')
        elif 2 <= self.skala <= 4:
            print('Gempa berdampak bangunan retak')
        elif 4 <= self.skala <= 6:
            print('Gempa berdampak bangunan roboh')
        elif self.skala > 6:
            print('Gempa besar berpotensi tsunami')

    # Menampilkan Lokasi Gempa dan Skala Gempa
        print(f'Lokasi Gempa: {self.skala}')
        print(f'Skala Gempa: {self.skala}')