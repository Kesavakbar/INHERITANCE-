class Kucing:
    def __init__(self, name, jenis):
        self.name = name
        self.jenis = jenis

    def visual(self):
        print("kucing itu bernama", self.name, ",dengan jenis", self.jenis)

def main():
    kucing1 = Kucing("anggi", "anggora")  
    kucing1.visual()

if __name__ == "__main__":
    main()