from robot import Robot
class Dinosaur:
    
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 3

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f'{self.name} attacked {robot.name} for {self.attack_power} damage')
        