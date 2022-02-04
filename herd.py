from dinosaur import Dinosaur

class Herd:


    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino_one = Dinosaur('Bio Engineered T-Rex', 20)
        dino_two = Dinosaur('Bio Engineered', 15)
        dino_three = Dinosaur('The Abomination', 30)
        self.dinosaurs.append(dino_one)
        self.dinosaurs.append(dino_two)
        self.dinosaurs.append(dino_three)
        pass
    