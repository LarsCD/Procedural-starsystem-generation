import random
from physics_calculator import Calculate

# for planetary data: https://elite-dangerous.fandom.com/wiki/Planets
# atmospheric data: https://en.wikipedia.org/wiki/Extraterrestrial_atmosphere

class Planet:
    def __init__(self,name,type,type_name,mass,gravity,g,radius,has_atmosphere,has_ring,spawn_chance):
        self.name = name
        self.type = type
        self.type_name = type_name
        self.mass = mass
        self.gravity = gravity
        self.g = g
        self.radius = radius
        self.has_atmosphere = has_atmosphere
        self.has_ring = has_ring
        self.spawn_chance = spawn_chance


class Atmosphere:
    def __init__(self,has_atmosphere):
        self.has_atmosphere = has_atmosphere



class Generator:
    def __init__(self):
        self.Calculate = Calculate()

    def generate_planet(self, planetary_data, meta_data, seed, planetary_body_type=None, planetary_body_class=None):
        # variables
        class_weights_list = []

        # data flow: generated_planet -> decorated_planet -> completed_planet -> return
        generated_planet = {}
        decorated_planet = {}
        completed_planet_object = 'None'

        # set seed to random
        random.seed(seed)

        # if planetary_body_type and planetary_body_class are not provided,
        # generate random planetary body type and class
        if planetary_body_type is None and planetary_body_class is None:
            # get planetary_body_type based on spawn rate
            planetary_body_type = random.choices(
                list(planetary_data.keys()),
                weights=meta_data['spawn_rate_weights'])

            # make list of weights based on planetary_body_type spawn rate
            for object in planetary_data[planetary_body_type[0]].values():
                weight = object['spawn_rate']
                class_weights_list.append(weight)

            # get planetary_body_class based on planetary_body_type spawn rate
            planetary_body_class = random.choices(
                list(planetary_data[planetary_body_type[0]]),
                weights=class_weights_list)

        # if planetary_body_type is provided but planetary_body_class is not,
        # generate random planetary body class for the given type
        elif planetary_body_type is not None and planetary_body_class is None:
            # make list of weights based on planetary_body_type spawn rate
            for object in planetary_data[planetary_body_type].values():
                weight = object['spawn_rate']
                class_weights_list.append(weight)

            # get planetary_body_class based on planetary_body_type spawn rate
            planetary_body_class = random.choices(
                list(planetary_data[planetary_body_type]),
                weights=class_weights_list)

        # if both planetary_body_type and planetary_body_class are provided,
        # use them to generate the specified planetary body
        elif planetary_body_type is not None and planetary_body_class is not None:
            planetary_body_type = planetary_body_type
            planetary_body_class = planetary_body_class

        # if planetary_body_type is a string, wrap it in a list
        if isinstance(planetary_body_type, str):
            planetary_body_type = [planetary_body_type]

        # if planetary_body_class is a string, wrap it in a list
        if isinstance(planetary_body_class, str):
            planetary_body_class = [planetary_body_class]

        # get planetary body data
        generated_planet = planetary_data[planetary_body_type[0]][planetary_body_class[0]]

        # decorated_planet becomes placeholder to recieve randomly generated attributes
        decorated_planet = generated_planet

        # generate attributes
        radius = random.randint(generated_planet['radius_indicator'][0], generated_planet['radius_indicator'][1])
        density = random.uniform(generated_planet['density_indicator'][0], generated_planet['density_indicator'][1])
        if (random.randint(0, 100) <= generated_planet['has_atmosphere_chance']):
            has_atmosphere = True
        else:
            has_atmosphere = False
        if (random.randint(0, 100) <= generated_planet['has_ring_chance']):
            has_ring = True
        else:
            has_ring = False
        mass = round((self.Calculate.mass(radius * 1000, density * 1000)), 3)
        gravity = round((self.Calculate.gravity(mass, radius*1000)), 2)
        g = round(self.Calculate.g(gravity), 2)

        name = generated_planet['name']
        type = generated_planet['type']
        type_name = generated_planet['type_name']

        # calculate spawn chance
        planetary_body_index = list(planetary_data.keys()).index(planetary_body_type[0])
        spawn_chance_type = meta_data['spawn_rate_weights'][planetary_body_index]
        spawn_chance_class = generated_planet['spawn_rate']

        spawn_chance = round((((spawn_chance_type / 100) / (1 / spawn_chance_class))), 3)

        # give attributes to planet
        completed_planet_object = Planet(name, type, type_name, mass, gravity, g, radius, has_atmosphere, has_ring,
                                                   spawn_chance)
        return completed_planet_object



    def generate_atmosphere_composition(self):
        pass
