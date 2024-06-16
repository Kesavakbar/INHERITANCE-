class Animal():
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def visual(self):
        print("kucing ini bernama", self.nama, "dengan jenis", self.jenis)

class Apa(Animal):
    def __init__(self,nama, jenis, warna):
            super().__init__(nama, jenis)
            self.warna = warna

    def visual(self):
        print("kucing ini bernama", self.nama, "dengan jenis", self.jenis, "memiliki warna", self.warna)

class Goldar(Animal):
     def __init__(self, nama, jenis, warna, tipe):
          super().__init__(nama, jenis)
          self.tipe = tipe
          self.warna = warna

     def visual(self):
        print("kucing ini bernama", self.nama, "dengan jenis", self.jenis, "memiliki warna", self.warna, "dengan tipe", self.tipe)



def main():
    animal1 = Animal("Anggi", "anggora")
    animal2 = Apa("Bila", "Anggora", "merah")
    animal3 = Goldar("Junkook", "persian", "oren", "loreng")
    animal1.visual()
    animal2.visual()
    animal3.visual()

if __name__ == "__main__":
    main()
