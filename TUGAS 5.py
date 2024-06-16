# parent class

class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoIsThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class

class Pinguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def whoIsThis(self):
        print("Penguin")

    def Run(self):
        print("Run faster")

peggy = Pinguin()
peggy.whoIsThis()
peggy.swim()
peggy.Run()