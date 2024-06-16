class Manusia:
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur

    def informasi(self):
        print("dia adalah", self.nama, ", dengan usia", self.umur)

def main():
    manusia1 = Manusia("Anis", 42)
    manusia1.informasi()
if __name__ == "__main__":
    main()