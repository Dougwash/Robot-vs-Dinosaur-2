from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self):
        self.robot = Robot('Killer Bot')
        self.dinosaur = Dinosaur("T Rex",15)
        # self.robot = robot
        # self.dinosaur = dinosaur
        pass

    def run_game (self):
        Battlefield.display_welcome(self)
        Battlefield.battle_phase(self)
        Battlefield.winner(self)



    def display_welcome (self):
        print('\nWelcome to Robot Vs Dinasaur \n who will win...\n')

    def battle_phase (self):
        while self.dinosaur.health > 0 and self.robot.health >0:

            Dinosaur.attact(self)
            if self.robot.health >0:
                Robot.robo_attact(self)
        # elif self.dinosaur.health >0:
        #     Battlefield.battle_phase(self)

        # Battlefield.winner(self)


    def winner (self):
        if self.dinosaur.health == 0:
            print(f"Robot: {self.robot.name} wins\n")
        elif self.robot.health == 0:
            print(f'Dino: {self.dinosaur.name} Won\n')
        
        # pass

