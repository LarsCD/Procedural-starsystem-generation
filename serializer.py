import json
import traceback

class Serializer:
    def __init__(self):
        pass

    def load_config(self):
        data = None
        print('> Loading config_data from \'config.json\'')
        try:
            with open('data/config.json', 'r') as file:
                data = json.load(file)
        except Exception:
            print(f'> ERROR: Failure loading config_data from \'config.json\'\n> {traceback.print_exc()}')
        else:
            print(f'> Successfully loaded config_data from \'config.json\'')
        return data


    def load_planet_data(self, filename):
        data = None
        print(f'> Loading planetary_data from \'{filename}\'')
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except Exception:
            print(f'> ERROR: Failure loading planet_data from \'{filename}\'\n> {traceback.print_exc()}')
        else:
            print(f'> Successfully loaded planet_data from \'{filename}\'')
        return data


    def load_compound_data(self, filename):
        data = None
        print(f'> Loading compound_data from \'{filename}\'')
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except Exception:
            print(f'> ERROR: Failure loading compound_data from \'{filename}\'\n> {traceback.print_exc()}')
        else:
            print(f'> Successfully loaded compound_data from \'{filename}\'')
        return data


    def load_stellar_data(self, filename):
        data = None
        print(f'> Loading stellar_data from \'{filename}\'')
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except Exception:
            print(f'> ERROR: Failure loading stellar_data from \'{filename}\'\n> {traceback.print_exc()}')
        else:
            print(f'> Successfully loaded stellar_data from \'{filename}\'')
        return data
    

    def load_starsystem_config(self, filename):
        data = None
        print(f'> Loading starsystem_config from \'{filename}\'')
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except Exception:
            print(f'> ERROR: Failure loading starsystem_config from \'{filename}\'\n> {traceback.print_exc()}')
        else:
            print(f'> Successfully loaded starsystem_config from \'{filename}\'')
        return data