class Rechteck:

    def __init__(self, laenge, breite):
        self.myLaenge = laenge
        self.myBreite = breite

        print('rechteck erstellt')
        pass

    def printRechteck(self):
        print('Das Rechteck hat die Laenge ' + str(self.myLaenge) +' und die Breite ' + str(self.myBreite))

    def calcUmfang(self):
        return 2*self.myBreite + 2*self.myLaenge

    def calcFI(self):
        return self.myBreite * self.myLaenge

    def hasBiggerFI(self, other):
        selfFI = self.calcFI()
        otherFI = other.calcFI()
        return selfFI > otherFI

rechteck1 = Rechteck(10, 4)

rechteck1.printRechteck()

rechteck2 = Rechteck(20,2)

print(rechteck1.calcFI())
print(rechteck2.calcFI())

if rechteck1.hasBiggerFI(rechteck2):
    print('rechteck 1 ist groesser')
else:
    print('rechteck ist kleiner oder gleich')