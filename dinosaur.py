from robot import Robot
class Dinosaur:
    
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 3
    def __str__(self):
        return f'Dino name: {self.name} HP: {self.health} Attack Power: {self.attack_power}'
    
    def attack(self, robot):
        robot.health -= self.attack_power
        print(f'{self.name} attacked {robot.name} for {self.attack_power} damage, {robot.name} has {robot.health} health remaining')
    
    # def attack(self, fleet):
    #     fleet.robot.health -= self.attack_power
    #     print(f'{self.name} attacked {fleet.robot.name} for {self.attack_power} damage')
        