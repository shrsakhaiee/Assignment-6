class Fraction:
    def __init__(self, s, m):
        self.sorat = s
        self.makhraj = m
    
    def add(self, frac):
        result = Fraction(1, 1)
        result.sorat = ( self.sorat * frac.makhraj) + (frac.sorat * self.makhraj)
        result.makhraj = self.makhraj * frac.makhraj
        return result

    def Submission(self, frac):
        result = Fraction(1, 1)
        result.sorat = (self.sorat * frac.makhraj) - (frac.sorat * self.makhraj)
        result.makhraj = self.makhraj * frac.makhraj
        return result

    def Multiplication(self, frac):
        result = Fraction(1, 1)
        result.sorat = self.sorat * frac.sorat
        result.makhraj = self.makhraj * frac.makhraj
        return result

    def Division(self, frac):
        result = Fraction(1, 1)
        result.sorat = self.sorat * frac.makhraj
        result.makhraj = self.makhraj * frac.sorat
        return result

    def sadekardan(self):
        while(True):
            if self.sorat % 2 == 0 and self.makhraj % 2 == 0:
                self.sorat //= 2
                self.makhraj //= 2

            elif self.sorat % 3 == 0 and self.makhraj % 3 == 0:
                self.sorat //= 3
                self.makhraj //= 3

            elif self.sorat % 5 == 0 and self.makhraj % 5 == 0:
                self.sorat //= 5
                self.makhraj //= 5

            elif self.sorat % 7 == 0 and self.makhraj % 7 == 0:
                self.sorat //= 7
                self.makhraj //= 7
            
            else:
                break
    
    def show(self):
        print(self.sorat, "/", self.makhraj)

f1 = Fraction(3, 5)
f2 = Fraction(1, 2)

f1.sadekardan()
f1.show()