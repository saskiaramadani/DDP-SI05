from Animals import *

class burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu = jenis_bulu
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print(f'hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}')

#object pertama
print('----- cetak burung -----')
print('----objek pertama -----')
beo = burung('burung beo', 'biji-bijian', 'udara', 'bertelur', 'blue and orange', 'hello')
beo.cetak_burung()

# object kedua
elang = burung('burung elang', 'daging', 'udara', 'bertelur', 'coklat and putih', 'hii')
elang.cetak_burung()


