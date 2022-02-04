from robot import Robot

class Fleet:

    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self): # make 3 robots here and append them to the list 
        robot_one = Robot("Tobor")
        robot_two = Robot("Colusses")
        robot_three = Robot("Kronos")
        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three)



    