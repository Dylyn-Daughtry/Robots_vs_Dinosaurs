from fleet import Fleet
from herd import Herd

class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.fleet.robots[0].attack(self.herd.dinosaurs[0]) # TESTED 

    def display_welcome(self):
        print('The testing arena')

    def battle(self): # while both teams list are longer than 0
        self.fleet.robots
        self.herd.dinosaurs
    
    def dino_turn(self, dinosaur): # get one round of dino attackds to work the way you want, then call this in battle
        dinosaur.attack
        pass

    def robo_turn(self, robot):# get one round of robot attackds to work the way you want, then call this in battle
        robot.attack
        pass

    def show_dino_opponent_options(self): # this can be used to do a for loop and show the user the avaialbe options 
        pass

    def show_robo_opponent_options(self): # this can be used to do a for loop and show the user the avaialbe options 
        pass

    def display_winners(self):
        pass
    
    
        
