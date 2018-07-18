import robots

class Roboter:

    def __init__(self, name, baujahr):
        self.name = name
        self.baujahr = baujahr

    def SageHallo(self):
        print("Hallo, mein Name ist " + self.name)

    def NeuerName(self):
        self.name = name

    def HoleNamen(self):
        return self.name

    def NeuesBaujahr(self, baujahr):
        self.baujahr = baujahr

    def HoleBaujahr(self):
        return str(self.baujahr)

if __name__ == "__main__":
    x = Roboter("Marvin", "1975")
    y = Roboter("Caliban", "1985")
    z = Roboter("Brot", "1927")
    for rob in [x, y, z]:
        rob.SageHallo()
        print("Ich bin " + rob.HoleBaujahr() + " erschaffen worden!")
