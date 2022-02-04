from weapon import Weapon

class Arsenal:

    def __init__(self):
        self.weapons = []
        self.create_arsenal()

    def create_arsenal(self):  
        weapon_one = Weapon("Sword", 2)
        weapon_two = Weapon("Knife", 1)
        weapon_three = Weapon("Axe", 3)
        self.weapons.append(weapon_one)
        self.weapons.append(weapon_two)
        self.weapons.append(weapon_three)
