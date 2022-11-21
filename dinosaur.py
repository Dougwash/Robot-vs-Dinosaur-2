

class Dinosaur:
    def __init__(self, name, attact_power):
        self.name=name
        self.attact_power = attact_power
        self.health = 100


    def attact (self):
        while self.robot.health > 0:
            self.robot.health -= self.dinosaur.attact_power
            print(f'{self.dinosaur.name} has attacted {self.robot.name} \n with %{self.robot.health} health remaining\n')
            return

        
        pass