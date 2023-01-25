import math

class Constants:
    def __init__(self):
        self.G = 6.6743e-11
        self.earth_g = 9.81             # m/s^2
        self.L_avogadro = 6.0221408e23  #
        self.R_gas = 8.3144598          # J/mol k
        self.C = 299_792_458            # m/s
        self.AU = 149_597_871           # km
        self.earth_mass = 5.97219e24    # kg
        self.solar_mass = 1.9891e30     # kg
        self.earth_day_seconds = 86_160 # s

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

    def average_atmospheric_persure(self, temperature, gravity, atmospheric_mass):
        # Constants
        R = self.Constants.R_gas
        T = temperature # in K
        g = gravity # in m/s^2
        M = atmospheric_mass # in kg

        # Calculate avg atmospheric pressure
        pressure = (g * M) / (R * T)  # in Pa
        return pressure

    def km_to_au(self, distance_km): # conversion
        distance_au = self.Constants.AU/distance_km
        return distance_au

    def orbital_time(self, radius_km, star_solar_mass): # kepler
        G = self.Constants.G
        m = star_solar_mass*self.Constants.solar_mass # kg
        r = radius_km *1000 # m
        # v = math.sqrt((G*m)/r) # m/s
        T = math.sqrt((4*(math.pi**2)*(r**3))/(G*m))
        return T






