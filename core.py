from serializer import Serializer
from generator import Generator
from physics_calculator import Calculate
import json
import random
from GUT import GUT, COLOR
import os
os.system("")
Fore = COLOR.Fore
Back = COLOR.Back


class Core:
    def __init__(self):
        self.planet_data_file_name = 'data/planet_data.json'
        self.Serializer = Serializer()
        self.Generator = Generator()
        self.Calculate = Calculate()
        self.primary_planet_data = self.Serializer.load_planet_data(self.planet_data_file_name)


    def update_game(self):
        print('run')
        click = input('[enter] to start generation')
        for i in range(10000):
            seed = int(round((i+1)))
            planetary_body = self.generate_planetary_body(
                seed,
            )
            print(f"Name:           {Fore.GREEN()}{planetary_body.name}{Fore.RESET()}")
            print(f"Type:           {Fore.B_BLUE()}{planetary_body.type_name}{Fore.RESET()}")
            print(f"Mass:           {planetary_body.mass} kg")
            print(f'Gravity:        {planetary_body.gravity} m/s')
            print(f'g:              {planetary_body.g} g')
            print(f"Radius:         {planetary_body.radius} km")
            print(f"Has atmosphere: {planetary_body.has_atmosphere}")
            print(f"Has ring:       {planetary_body.has_ring}")
            print(f"Spawn Chance:   {planetary_body.spawn_chance}%")
            print(f"Seed:           ({seed})")
            print('\n')
        print('success')
        click = input('[enter] to quit')

        print('success')


    def generate_planetary_body(self, seed, planetary_body_type=None, planetary_body_class=None):
        primary_data = self.primary_planet_data
        planetary_data, meta_data = primary_data['planetary_data'], primary_data['meta_data']
        planetary_object = self.Generator.generate_planet(
            planetary_data,
            meta_data,
            seed,
            planetary_body_type=planetary_body_type,
            planetary_body_class=planetary_body_class
        )
        return planetary_object