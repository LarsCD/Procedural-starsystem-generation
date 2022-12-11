import math

class Calculate:
    def __init__(self):
        pass

    def mass(self, radius, density):
        r = radius
        ρ = density # kg/m3
        v = (4/3)*(math.pi)*math.pow(r, 3) # m3
        m = ρ*v
        return m