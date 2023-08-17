class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale")


class Fish(Animal):                         # Inherit from animal class
    def __init__(self):
        super().__init__()                  # call super constructor

    def swim(self):
        print("SWIIIIIIM")

    def breathe(self):
        super().breathe()
        print("Doing this underwater")      # INHERITS BREATHE AND UPDATE


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)