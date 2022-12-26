import os
import sys
import random
import json

from serializer import Serializer
from generator import Generator
from physics_calculator import Calculate
from GUT import GUT, COLOR
from display import Display
os.system("")
Fore = COLOR.Fore
Back = COLOR.Back


class Core:
    def __init__(self):
        # filenames
        self.planet_data_filename = 'data/planet_data.json'
        self.compound_data_filename = 'data/compound_data.json'
        self.stellar_data_filename = 'data/stellar_data.json'
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
        self.static_stellar_data = self.Serializer.load_stellar_data(self.stellar_data_filename)


    def update_game(self):
        self.load_data()
        print('run')
        click = input('[enter] to start generation')

        universe_data = []
        gen_range = 100
        print(f'> Generating {gen_range} planetary bodies...')
        for i in range(gen_range):
            seed = random.randint(0, 9999999999)
            stellar_object = self.generate_star(seed)
            Display.display_star(stellar_object)
            # planetary_body = self.generate_planetary_body(seed)
            # universe_data.append(stellar_object)
            # universe_data.append(planetary_body)
            # Display.display_planet(planetary_body)
            print('\n\n')
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

    def generate_star(self, seed, stellar_type=None, stellar_class=None):
        primary_data = self.static_stellar_data
        stellar_data, meta_data = primary_data['stellar_data'], primary_data['meta_data']
        stellar_object = self.Generator.generate_star(
            stellar_data,
            meta_data,
            seed,
            stellar_type=stellar_type,
            stellar_class=stellar_class
        )
        return stellar_object
