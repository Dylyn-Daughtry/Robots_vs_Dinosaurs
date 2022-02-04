from dinosaur import Dinosaur

class Herd:


    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino_one = Dinosaur('TestRex', 2)
        dino_two = Dinosaur('Testodactyl', 1)
        dino_three = Dinosaur('Testrawr', 1)
        self.dinosaurs.append(dino_one)
        self.dinosaurs.append(dino_two)
        self.dinosaurs.append(dino_three)
        pass
    