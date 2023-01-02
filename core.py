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
        self.starsystem_config_filename = 'data/starsystem_config.json'
        # load components
        self.Serializer = Serializer()
        self.Generator = Generator()
        self.Calculate = Calculate()


    def load_data(self):
        self.static_planet_data = self.Serializer.load_planet_data(self.planet_data_filename)
        self.static_compound_data = self.Serializer.load_compound_data(self.compound_data_filename)
        self.static_stellar_data = self.Serializer.load_stellar_data(self.stellar_data_filename)
        self.static_starsystem_config = self.Serializer.load_starsystem_config(self.starsystem_config_filename)
        self.planetary_meta_data = self.static_planet_data['meta_data']
        self.stellar_meta_data = self.static_stellar_data['meta_data']
        


    def update_game(self):
        self.load_data()
        print('run')
        universe = []
        seed = random.randint(0, 999999999)
        # seed = 55176457
        starsystem = self.Generator.generate_system(
            self.static_starsystem_config,
            self.static_stellar_data,
            self.static_planet_data,
            self.static_compound_data,
            self.stellar_meta_data,
            self.planetary_meta_data,
            seed
        )
        for key in starsystem:
            print(f'{key}:  {starsystem[key]}')
        universe.append(starsystem)

        # for i in range(0, 100):
        #     name = self.Generator.system_name_generator(i+13)
        #     print(name)

        # print(starsystem)
        print('=============================================================================')
        click = input('exit')

        


    # def generate_planetary_body(self, seed, planetary_body_type=None, planetary_body_class=None):
    #     primary_data = self.static_planet_data
    #     planetary_data, meta_data = self.static_planet_data['planetary_data'], self.static_planet_data['meta_data']
    #     compound_data = self.static_compound_data
    #     planetary_object = self.Generator.generate_planet(
    #         planetary_data,
    #         compound_data,
    #         meta_data,
    #         seed,
    #         planetary_body_type=planetary_body_type,
    #         planetary_body_class=planetary_body_class
    #     )
    #     return planetary_object

    # def generate_star(self, seed, stellar_type=None, stellar_class=None):
    #     primary_data = self.static_stellar_data
    #     stellar_data, meta_data = primary_data['stellar_data'], primary_data['meta_data']
    #     stellar_object = self.Generator.generate_star(
    #         stellar_data,
    #         meta_data,
    #         seed,
    #         stellar_type=stellar_type,
    #         stellar_class=stellar_class
    #     )
    #     return stellar_object
