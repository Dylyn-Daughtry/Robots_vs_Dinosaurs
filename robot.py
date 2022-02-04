
class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 3
        self.weapon = None

    def __str__(self):
        return f'Robot name: {self.name} HP: {self.health}'
    
    def attack(self, dinosaur): # dino.health - self.weapon.attack_power   then use print statments to fill in the user what happend 
        dinosaur.health -= self.weapon.attack_power
        print(f'{self.name} dealt {self.weapon.attack_power} to {dinosaur.name}')
        print(f'{dinosaur.name} health is now {dinosaur.health}')
        
    def assign_weapon(self, weapon_selection):
        self.weapon = weapon_selection
        print(f'{self.name} has equipped a {self.weapon.name}' )
    