import os
import sys
import random
import json

from serializer import Serializer
from generator import Generator
from physics_calculator import Calculate
from GUT import GUT, COLOR
os.system("")
Fore = COLOR.Fore
Back = COLOR.Back


class Core:
    def __init__(self):
        # filenames
        self.planet_data_filename = 'data/planet_data.json'
        self.compound_data_filename = 'data/compound_data.json'
        # load components
        self.Serializer = Serializer()
        self.Generator = Generator()
        self.Calculate = Calculate()
        # static variables that stay unchanged
        self.static_planet_data = {}
        self.static_compound_data = {}

    def load_data(self):
        self.static_planet_data = self.Serializer.load_planet_data(self.planet_data_filename)
        self.static_compound_data = self.Serializer.load_compound_data(self.compound_data_filename)


    def update_game(self):
        self.load_data()
        print('run')
        click = input('[enter] to start generation')
        universe_data = []
        gen_range = 5
        print(f'> Generating {gen_range} planetary bodies...')
        for i in range(gen_range):
            seed = random.randint(0, 9999999999)
            planetary_body = self.generate_planetary_body(
                seed,
            )
            universe_data.append(planetary_body)
            print(f"Type:           {Fore.GREEN()}{planetary_body.type}{Fore.RESET()}")
            print(f"Class:          {Fore.B_BLUE()}{planetary_body._class}{Fore.RESET()}")
            print(f"Mass:           {planetary_body.mass} kg")
            print(f"Density:        {planetary_body.density} kg/L")
            print(f'Gravity:        {planetary_body.gravity} m/s')
            print(f'g:              {planetary_body.g} g')
            print(f"Radius:         {planetary_body.radius} km")
            print(f"Atmosphere:")
            for key in planetary_body.atmospheric_data:
                print(f'  - {Fore.CYAN()}{key}{Fore.RESET()}:  {planetary_body.atmospheric_data[key]}')
            print(f"Has ring:       {planetary_body.has_ring}")
            print(f"Spawn Chance:   {planetary_body.spawn_chance}%")
            print(f"Seed:           ({seed})")
            print(f'[BYTE SIZE]:    [{(sys.getsizeof(planetary_body))} bytes]')
            print('\n\n\n')
        print(f'> Successfully generated {gen_range} planetary bodies')
        print(f'[TOTAL SIZE]:    [{(sys.getsizeof(universe_data))/1000} kb]')
        click = input('[enter] to quit')
        print('success')


    def generate_planetary_body(self, seed, planetary_body_type=None, planetary_body_class=None):
        primary_data = self.static_planet_data
        planetary_data, meta_data = self.static_planet_data['planetary_data'], self.static_planet_data['meta_data']
        compound_data = self.static_compound_data
        planetary_object = self.Generator.generate_planet(
            planetary_data,
            compound_data,
            meta_data,
            seed,
            planetary_body_type=planetary_body_type,
            planetary_body_class=planetary_body_class
        )
        return planetary_object
