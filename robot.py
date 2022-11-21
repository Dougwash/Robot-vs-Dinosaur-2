from weapon import Weapon

weapon = Weapon('lazer eys',20)

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = weapon


    def robo_attact (self):
         while self.dinosaur.health > 0:
            self.dinosaur.health -= weapon.attact_power
            # print(self.dinosaur.name,self.dinosaur.health)
            print(f'{self.robot.name} has attacted {self.dinosaur.name} \n with %{self.dinosaur.health} health remaining\n')

            return

# Robot.robo_attact()   