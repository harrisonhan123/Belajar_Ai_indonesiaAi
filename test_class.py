# class Cat:
#     '''
#     ini adalah class utk membuat objek kucing
#     '''
#     spesies = 'Kucing'

#     def __init__(self,nama,tipe):
#         self.nama = nama
#         self.tipe = tipe

#     def run(self,speed):
#         print(f"Kucing {self.nama} berlari dengan {speed}")

#     def play(self):
#         pass
#     def eat(self):
#         pass

# membuat objek
# kinako = Cat(nama='kinako',tipe='anggora')
# print(kinako)
# print(f"{kinako.nama} adalah seekor {kinako.__class__.spesies}")
# kinako.run('cepat')

# print(kinako.__doc__)


# GETTER & SETTER
# class Mobil:
#     def __init__(self,plat):
#         self.plat = plat
#         self.__tipe = "avanza"    # PRIVATE 
#         self.__bensin = 40 #liter

#     getter
#     def lihatMaksimumBensin(self):
#         print(f"Maksimum bensin = {self.__bensin} liter")

#     setter
#     def aturMaksimumBensin(self,bensin):
#         self.__bensin=bensin

# Avanza = Mobil(plat="B 7185 XC")

# print(Avanza.plat)
# print(Avanza.tipe)
# print(Avanza.bensin)

# Avanza.bensin=30
# print(Avanza.bensin)

# Avanza.lihatMaksimumBensin()

# Avanza.aturMaksimumBensin(100)
# Avanza.lihatMaksimumBensin()

#INHERITANCE
#parrent Class
# class Animal:
#     def __init__(self):
#         self.tipe = "Mamalia"
#         self.kecepatan = "Lambat"

#     def grow(self):
#         print("Mamalia ini bertumbuh")

# #chlid class
# class Cat(Animal):
#     def __init__(self,nama,tipe):
#         super().__init__()  #OVERRIDDING
#         self.nama = nama
#         self.tipe = tipe
#     def run(self):
#         print(f"Kucing {self.tipe} ini berlari ...")

# kinako = Cat(nama='Kinako', tipe='Anggora')
# print(kinako.kecepatan)   
# print(kinako.tipe) 
# kinako.grow()
# kinako.run()

#POLIMORPHISM
class Cat:
    def __init__(self):
        self.name="meong"
        self.tipe="anggora"
    def forward(self):
        print("Kucing berlalri")

class Bird:
    def __init__(self):
        self.name="erago"
        self.tipe="elang"
    def forward(self):
        print("Burung terbang")

def melaju(objek):
    objek.forward()

meong = Cat()
erago = Bird()

melaju(meong)
melaju(erago)