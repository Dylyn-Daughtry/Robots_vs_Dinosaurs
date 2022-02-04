from weapon import Weapon


class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 3
        self.weapon = Weapon("Sword", 1)
    
    def attack(self, dinosaur): # dino.health - self.weapon.attack_power   then use print statments to fill in the user what happend 
        dinosaur.health -= self.weapon.attack_power
        print(f'{self.name} dealt {self.weapon.attack_power} to {dinosaur.name}')
        print(f'{dinosaur.name} health is now {dinosaur.health}')
        

