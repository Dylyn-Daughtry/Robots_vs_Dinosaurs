from fleet import Fleet
from herd import Herd
# from weapon import Weapon
from arsenal import Arsenal
class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.arsenal = Arsenal()
    
    def run_game(self):
        self.display_welcome()
        #self.fleet.robots[0].attack(self.herd.dinosaurs[0]) # TESTED 
        self.battle()
        self.display_winners()

    def display_welcome(self):
        print()
        print('Welcome to the test arena')
        print()
        print('Team Heavy Metal:')
        for robot in self.fleet.robots:
            print(robot)
        print()
        print()
        print('Team Veloci-Fact-ors!:')
        for dinosaur in self.herd.dinosaurs:
            print(dinosaur)
        print()
        print()


    def battle(self): # while both teams list are longer than 0
        self.select_robot()
        current_robot = int(input()) - 1
        print()
        self.select_robot_weapon()  
        self.fleet.robots[current_robot].assign_weapon(self.arsenal.weapons[int(input()) - 1])   
        print()
        # self.show_dino_options()
        # current_dino = int(input())
        # current_robot = 0
        current_dino = 0
        while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:      # swap out health for length of list, need to add logic to remove opponents with 0 or less health
           self.robo_turn(self.herd.dinosaurs[current_dino], self.fleet.robots[current_robot])
           if self.herd.dinosaurs[current_dino].health <= 0:
               self.herd.dinosaurs.remove(self.herd.dinosaurs[current_dino])
           print()
           if len(self.herd.dinosaurs) > 0:
                self.dino_turn(self.fleet.robots[current_robot], self.herd.dinosaurs[current_dino])
                if self.fleet.robots[current_robot].health <= 0:
                    self.fleet.robots.remove(self.fleet.robots[current_robot])
                    # self.arsenal.weapons.remove(self.fleet.robots[current_robot].weapon)
                    if len(self.fleet.robots) > 0:
                        print()
                        self.select_robot()
                        current_robot = int(input()) - 1
                        print()
                        self.select_robot_weapon()
                        self.fleet.robots[current_robot].assign_weapon(self.arsenal.weapons[int(input()) - 1]) 
                        print()
           print()
            
    
    def dino_turn(self,robot, dinosaur): # get one round of dino attackds to work the way you want, then call this in battle
        dinosaur.attack(robot)
        pass

    def robo_turn(self,dino, robot):# get one round of robot attackds to work the way you want, then call this in battle
        robot.attack(dino)
        pass

    def show_dino_options(self): # this can be used to do a for loop and show the user the avaialbe options 
        count = 0
        for dino in self.herd.dinosaurs:
            print(f'Input {count} to select {dino.name}')
            count += 1
        

    def select_robot(self): # this can be used to do a for loop and show the user the avaialbe options 
        count = 0
        for robot in self.fleet.robots:
            print(f'Input {count + 1} to select {robot.name}')
            count += 1
        
    def select_robot_weapon(self):
        count = 0
        for weapon in self.arsenal.weapons:
            print(f'Input {count + 1} to select {weapon.name}')
            count += 1
   
   
    def display_winners(self):
        if len(self.fleet.robots) == 0:
            print('Dinos Win')
        else:
            print('Skynet')
        print()
        print()
        print()    
    
        
