import sys
from colorama import Fore, Back, Style

# Define a function to display information about a planet
def display_planet(name, type, mass, radius):
    # Use ASCII characters to draw the planet
    planet_string = "o"
    atmosphere_string = "=" * (radius // 10)
    print(Fore.BLUE + planet_string + Fore.RESET)
    print(Fore.CYAN + atmosphere_string + Fore.RESET)

    # Display the planet's name, type, mass, and radius
    print(Fore.YELLOW + "Planet: " + Fore.RESET + name)
    print(Fore.YELLOW + "Type: " + Fore.RESET + type)
    print(Fore.YELLOW + "Mass: " + Fore.RESET + str(mass) + " kg")
    print(Fore.YELLOW + "Radius: " + Fore.RESET + str(radius) + " km")

# Generate a random planet
name = "Earth"
type = "Terrestrial"
mass = 5.972 * 10 ** 24
radius = 6371

# Display the planet
display_planet(name, type, mass, radius)
click = input('[enter] to exit')
