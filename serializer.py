import json

class Serializer:
    def __init__(self):
        pass

    def load_config(self):
        print('> Loading config_data from \'config.json\'')
        try:
            with open('data/config.json', 'r') as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(f'> ERROR: Failure loading config_data from \'config.json\'')
        else:
            print(f'> Successfully loaded config_data from \'config.json\'')

    def load_planet_data(self, filename):
        print(f'> Loading planetary data from \'{filename}\'')
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(f'> ERROR: Failure loading planet_data from \'{filename}\'')
        else:
            print(f'> Successfully loaded planet_data from \'{filename}\'')