from robot import Robot

class Fleet:

    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self): # make 3 robots here and append them to the list 
        robot_one = Robot("testbot")
        robot_two = Robot("testbot2")
        robot_three = Robot("testbot3")
        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three)



    