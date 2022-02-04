from weapon import Weapon

class Arsenal:

    def __init__(self):
        self.weapons = []
        self.create_arsenal()

    def create_arsenal(self):  
        weapon_one = Weapon("Rusty Knuckles", 14)
        weapon_two = Weapon("Shock Cannon", 25)
        weapon_three = Weapon("Flame thrower", 20)
        weapon_four = Weapon("Rocket Fist", 18)
        self.weapons.append(weapon_one)
        self.weapons.append(weapon_two)
        self.weapons.append(weapon_three)
        self.weapons.append(weapon_four)
