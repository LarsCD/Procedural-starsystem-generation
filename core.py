from serializer import Serializer
from generator import Generator
from physics_calculator import Calculate
import json
import random


class Core:
    def __init__(self):
        self.planet_data_file_name = 'planet_data.json'
        self.Serializer = Serializer()
        self.Generator = Generator()
        self.Calculate = Calculate()
        self.primary_planet_data = self.Serializer.load_planet_data(self.planet_data_file_name)


    def update_game(self):
        print('run')
        click = input('[enter] to start generation')
        for i in range(10):
            seed = int(round((i+1)*(i*12)))
            planetary_body = self.generate_planetary_body(seed, planetary_body_type='dwarf_planet')
            print(f"Name: {planetary_body.name}")
            print(f"Type: {planetary_body.type}")
            print(f"Mass: {planetary_body.mass} kg")
            print(f"Radius: {planetary_body.radius} km")
            print(f"Has atmosphere: {planetary_body.has_atmosphere}")
            print(f"Has ring: {planetary_body.has_ring}")
            print(f"Spawn Chance: {planetary_body.spawn_chance}%")
            print(f"Seed: {seed}")
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