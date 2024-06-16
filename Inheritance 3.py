class Band():
    def __init__(self,nama, genre):
        self.nama = nama
        self.genre = genre

    def informasi(self):
        print(self.nama, "merupakan sebuah band yang memiliki aliran", self.genre)

class Musik(Band):
    def __init__(self,nama, genre, asal):
        super().__init__(nama,genre)
        self.asal = asal
    
    def informasi(self):
        print(self.nama,"adalah band yang memiliki aliran", self.genre, "style.", "Mereka juga berasal dari", self.asal)

def main():
    band1 = Musik("Armada", "POP", "Bandung")
    band2 = Band("Hindia", "POP")
    band1.informasi()
    band2.informasi()

if __name__=="__main__":
    main()


    