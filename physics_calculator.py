import math

class Constants:
    def __init__(self):
        self.G = 6.6743e-11
        self.earth_g = 9.81
        self.L_avogadro = 6.0221408e23

class Calculate:
    def __init__(self):
        self.Constants = Constants()

    def mass(self, radius, density):
        r = radius
        ρ = density # kg/m3
        v = (4/3)*(math.pi)*math.pow(r, 3) # m3
        m = ρ*v
        return m

    def gravity(self, mass, radius):
        M = mass
        R = radius
        G = self.Constants.G
        g = G*(M/math.pow(R, 2))
        return g

    def g(self, gravity):
        g = gravity/self.Constants.earth_g
        return g

