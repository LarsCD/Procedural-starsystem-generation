import math
import random

from physics_calculator import Calculate, Constants


# for planetary data:
# https://elite-dangerous.fandom.com/wiki/Planets

# atmospheric data:
# https://en.wikipedia.org/wiki/Extraterrestrial_atmosphere

# stellar data:
# https://www.astronomy.ohio-state.edu/ryden.1/ast162_2/notes8.html

class Planet:
    def __init__(self,type,_class,type_name,science_data,mass,density,gravity,g,radius,atmospheric_data,has_ring,data,seed,spawn_chance):
        self.type = type
        self.id = data['id']
        self._class = _class
        self.type_name = type_name
        self.science_data = science_data
        self.mass = mass
        self.density = density
        self.gravity = gravity
        self.g = g
        self.radius = radius
        self.atmospheric_data = atmospheric_data
        self.has_ring = has_ring
        self.distance = data['distance']
        self.orbital_period = data['orbital_period_days']
        self.seed = seed
        self.spawn_chance = spawn_chance

class Star:
    def __init__(self, name,_class,type,type_name,science_data,mass_solar,mass_kg,temperature,data,seed,spawn_chance):
        self.name = name
        self.id = data['id']
        self._class = _class
        self.type = type
        self.type_name = type_name
        self.science_data = science_data
        self.mass_solar = mass_solar
        self.mass_kg = mass_kg
        self.temperature = temperature
        self.seed = seed
        self.spawn_chance = spawn_chance



class Generator:
    def __init__(self):
        self.Calculate = Calculate()
        self.Constants = Constants()
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
        self.vowels = ['A', 'E', 'I', 'O', 'U']
        self.suffix = ['Prime', 'Ultimate', 'Convax', 'Sector', 'I', 'II', 'III', 'IV', 'V']


    def generate_system(self, static_starsystem_config, static_stellar_data, static_planetary_data, static_compound_data, stellar_meta_data, planetary_meta_data, seed):
        random.seed(seed)
        
        # variables
        starsystem_stars = [1,2]
        planet_distance_last = 0.15 # in AU

        star_index = 1      # counts index number of star
        planet_index = 1    # counts index number of planet
        combined_stellar_solar_mass = 0
        furtherst_planet = 0


        # data attributes
        system_name = 'PLACEHOLDER-SYSTEM-NAME'
        star_list = []
        planet_list = []
        starsystem_data = {}


        # generate how many bodies
        star_spawn_rates = static_starsystem_config['star_spawn_weights']
        starsystem_data['name'] = self.system_name_generator(seed)
        star_count = random.choices(starsystem_stars, star_spawn_rates)[0]
        planet_count = random.randint(3, 14)


        # generate extra data for star
        for i in range(star_count):
            data = {}
            data['class_index'] = i
            data['id'] = self.ID_generator_star(starsystem_data, data)
            star_seed = random.randint(0, 999999999999)
            stellar_object = self.generate_star(static_stellar_data, stellar_meta_data, data, star_seed)
            star_list.append(stellar_object)


        # calculate combined stellar mass
        for star in star_list:
            combined_stellar_solar_mass += star.mass_solar
        


        # generate extra data for planet 
        for i in range(planet_count):
            data = {}
            planet_seed = random.randint(0, 999999999999)
            data['class_index'] = int(i)
            data['id'] = self.ID_generator_planet(starsystem_data, data)
            data['distance'] = planet_distance_last*round(random.uniform(1.4, 2.0), 1)
            planet_distance_last = data['distance']
            distance_km = data['distance'] * self.Constants.AU
            data['orbital_period_days'] = (self.Calculate.orbital_time(distance_km, combined_stellar_solar_mass))/self.Constants.earth_day_seconds


            planetary_object = self.generate_planet(static_planetary_data, static_compound_data, planetary_meta_data, data, planet_seed)

            planet_list.append(planetary_object)
        furtherst_planet = planet_list[-1].distance


        # starsystem_data['system_id'] =
        starsystem_data['stars'] = star_list
        starsystem_data['planets'] = planet_list
        starsystem_data['system_populated'] = bool(random.getrandbits(1))
        starsystem_data['system_discovered'] = False
        starsystem_data['system_seed'] = seed
        starsystem_data['total_solar_mass'] = combined_stellar_solar_mass
        starsystem_data['star_count'] = len(star_list)
        starsystem_data['planet_count'] = len(planet_list)
        starsystem_data['furthest_point'] = furtherst_planet

        return starsystem_data


    def generate_star(self, stellar_data, meta_data, data, seed, stellar_type=None, stellar_class=None):
        class_weights_list = []

        generated_star = {}
        decorated_star = {}
        completed_star_object = None
        static_stellar_data = stellar_data['stellar_data']
        stellar_meta_data = meta_data

        random.seed(seed)

        if stellar_type is None and stellar_class is None:
            # get stellar_type based on spawn rate
            stellar_type = random.choices(
                list(static_stellar_data.keys()),
                weights=stellar_meta_data['spawn_rate_weights'])

            # make list of weights based on stellar_type spawn rate
            for object in static_stellar_data[stellar_type[0]].values():
                weight = object['spawn_rate']
                class_weights_list.append(weight)

            # get stellar_class based on stellar_type spawn rate
            stellar_class = random.choices(
                list(static_stellar_data[stellar_type[0]]),
                weights=class_weights_list)

        # if stellar_type is provided but stellar_class is not,
        # generate random planetary body class for the given type
        elif stellar_type is not None and stellar_class is None:
            # make list of weights based on stellar_type spawn rate
            for object in static_stellar_data[stellar_type].values():
                weight = object['spawn_rate']
                class_weights_list.append(weight)

            # get stellar_class based on stellar_type spawn rate
            stellar_class = random.choices(
                list(static_stellar_data[stellar_type]),
                weights=class_weights_list)

        # if both stellar_type and stellar_class are provided,
        # use them to generate the specified planetary body
        elif stellar_type is not None and stellar_class is not None:
            stellar_type = stellar_type
            stellar_class = stellar_class

        # if stellar_type is a string, wrap it in a list
        if isinstance(stellar_type, str):
            stellar_type = [stellar_type]

        # if stellar_class is a string, wrap it in a list
        if isinstance(stellar_class, str):
            stellar_class = [stellar_class]

        # get stellar data
        generated_star = static_stellar_data[stellar_type[0]][stellar_class[0]]

        # decorated_star becomes placeholder to recieve randomly generated attributes
        decorated_star = generated_star

        name = generated_star['name']
        type_name = generated_star['type_name']

        mass = round(random.uniform(generated_star['mass'][0], generated_star['mass'][1]), 1)
        if 'temperature' in generated_star:
            temperature = round(random.uniform(generated_star['temperature'][0], generated_star['temperature'][1]), 1)
        else:
            temperature = 'n/a'

        mass_kg = mass * self.Constants.solar_mass
        mass_solar = mass

        # calculate spawn chance
        stellar_body_index = list(static_stellar_data.keys()).index(stellar_type[0])
        spawn_chance_type = stellar_meta_data['spawn_rate_weights'][stellar_body_index]
        spawn_chance_class = generated_star['spawn_rate']

        spawn_chance = round((((spawn_chance_type / 100) / (1 / spawn_chance_class))), 3)
        science_data = round(1 / ((spawn_chance / 10) / 4) * 100) + random.randint(round(-(1 / spawn_chance * 200)),
                                                                                    round((1 / spawn_chance * 200)))

        # give attributes to star
        completed_star_object = Star(name,stellar_class,stellar_type,type_name,science_data,mass_solar,mass_kg,temperature,data,seed,spawn_chance)

        return completed_star_object


    def generate_planet(self, planetary_data, static_compound_data, planetary_meta_data, data, seed, planetary_body_type=None, planetary_body_class=None):
        # variables
        class_weights_list = []

        # data flow: generated_planet -> decorated_planet -> completed_planet -> return
        generated_planet = {}
        decorated_planet = {}
        completed_planet_object = None
        static_planetary_data = planetary_data['planetary_data']

        # set seed to random
        random.seed(seed)

        # if planetary_body_type and planetary_body_class are not provided,
        # generate random planetary body type and class
        if planetary_body_type is None and planetary_body_class is None:
            # get planetary_body_type based on spawn rate
            planetary_body_type = random.choices(
                list(static_planetary_data.keys()),
                weights=planetary_meta_data['spawn_rate_weights'])

            # make list of weights based on planetary_body_type spawn rate
            for object in static_planetary_data[planetary_body_type[0]].values():
                weight = object['spawn_rate']
                class_weights_list.append(weight)

            # get planetary_body_class based on planetary_body_type spawn rate
            planetary_body_class = random.choices(
                list(static_planetary_data[planetary_body_type[0]]),
                weights=class_weights_list)

        # if planetary_body_type is provided but planetary_body_class is not,
        # generate random planetary body class for the given type
        elif planetary_body_type is not None and planetary_body_class is None:
            # make list of weights based on planetary_body_type spawn rate
            for object in static_planetary_data[planetary_body_type].values():
                weight = object['spawn_rate']
                class_weights_list.append(weight)

            # get planetary_body_class based on planetary_body_type spawn rate
            planetary_body_class = random.choices(
                list(static_planetary_data[planetary_body_type]),
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
        generated_planet = static_planetary_data[planetary_body_type[0]][planetary_body_class[0]]

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
        planetary_body_index = list(static_planetary_data.keys()).index(planetary_body_type[0])
        spawn_chance_type = planetary_meta_data['spawn_rate_weights'][planetary_body_index]
        spawn_chance_class = generated_planet['spawn_rate']

        # BELOW: maybe use for later
        # ring_spawn_chance = 0
        #
        # if has_atmosphere:
        #     ring_spawn_chance = generated_planet['has_ring_chance']

        spawn_chance = round((((spawn_chance_type / 100) / (1 / spawn_chance_class))), 3)
        science_data = round(1/(spawn_chance/10)*100)+random.randint(round(-(1/spawn_chance*100)), round((1/spawn_chance*100)))

        # generate atmosphere data (temperature = 293 K)
        atmospheric_data = self.generate_atmospheric_data(static_compound_data, radius, mass, type, gravity, has_atmosphere, seed)

        # give attributes to planet
        completed_planet_object = Planet(name, type, type_name, science_data, mass, density, gravity, g, radius, atmospheric_data, has_ring,
                                                   data, seed,spawn_chance)
        return completed_planet_object


    def generate_atmospheric_data(self, static_compound_data, radius, mass, type, gravity, has_atmosphere, seed, temperature=293.0):
        # - chemical composition
        # - atmosphere height
        # - pressure

        # general variables
        compound_data = static_compound_data['compounds']
        elements = static_compound_data['elements']


        # planetary varaiables

        planet_has_atmosphere = has_atmosphere
        planet_radius = radius
        planet_mass = mass
        planet_type = type
        planet_gravity = gravity
        planet_temperature = temperature
        random.seed(seed)

        def generate_atmospheric_composition(static_compound_data):
            # variables
            static_compounds = static_compound_data['compounds']
            atmosphere_composition = []
            atmospheric_compounds_percentages = {}
            atmospheric_compounds_atomic_weights = {}

            # generate random list of compounds comprising the atmosphere
            compound_choice_num = random.randint(2, len(static_compounds))
            compound_list = random.sample(sorted(static_compounds), compound_choice_num)

            # Assign a random percentage to each selected chemical compound and normalize percentages
            total_percentage = 0
            for key in compound_list:
                # Generate a random percentage
                percentage = random.uniform(0, 100 - total_percentage)
                # Add the percentage to the dictionary of compounds and their percentages
                atmospheric_compounds_percentages[key] = percentage
                total_percentage += round(percentage, 2)
            # Check if the sum of the percentages is less than 100
            if total_percentage < 100:
                # Calculate the difference between 100 and the current total percentage
                difference = 100 - total_percentage
                # Assign the difference to the last element in the compound_list
                if percentage < 0.001:
                    pass
                else:
                    atmospheric_compounds_percentages[compound_list[-1]] += round(difference, 2)
            # Check if the sum of the percentages is more than 100
            elif total_percentage > 100:
                # Calculate the difference between the current total percentage and 100
                difference = total_percentage - 100
                # Subtract the difference from the last element in the compound_list
                atmospheric_compounds_percentages[compound_list[-1]] -= round(difference, 2)

            # add atomic weight to each selected chemical compound
            for key in compound_list:
                atmospheric_compounds_atomic_weights[key] = static_compounds[key]

            # add percentage dict and atomic weight list to atmospheric_composition
            sorted(atmospheric_compounds_percentages.items(), key=lambda x: x[1], reverse=True)
            atmosphere_composition.append(atmospheric_compounds_atomic_weights)
            atmosphere_composition.append(atmospheric_compounds_percentages)

            # Return atmospheric_composition dictionary
            return atmosphere_composition

        def calculate_atmospheric_height(radius: float, mass: float):
            A = 0.00485
            atmospheric_height = radius*A
            return atmospheric_height

        def calculate_atmospheric_volume(radius: float, height: float):
            # function returns the volume of a planet's atmosphere
            outer_radius = (radius*1000+height*1000)
            inner_radius = radius*1000
            volume = (4 / 3 * math.pi * (outer_radius ** 3 - inner_radius ** 3))/1000000000
            return volume

        def calculate_atmospheric_mass(atmosphere_volume: float, atmospheric_composition: dict):
            mol_mass = 0
            # Calculate the molecular weight of the atmosphere
            for key in atmospheric_composition[0]:
                mol_mass += (atmospheric_composition[0][key] / 100) * atmospheric_composition[1][key]  # in kg/mol
            atmosphere_mass = (mol_mass*atmosphere_volume)
            return atmosphere_mass

        def calculate_atmospheric_pressure(temperature: float, gravity: float, atmospheric_mass: dict):

            # Calculate the maximum atmospheric pressure
            pressure = self.Calculate.average_atmospheric_persure(temperature, gravity, atmospheric_mass)/10000  # in Pa

            # Return the maximum atmospheric pressure
            return pressure

        if planet_has_atmosphere:
            # generate atmospheric data
            atmospheric_composition = generate_atmospheric_composition(static_compound_data)
            atmospheric_height = calculate_atmospheric_height(planet_radius, planet_mass)
            atmospheric_volume = calculate_atmospheric_volume(planet_radius, atmospheric_height)
            atmospheric_mass = calculate_atmospheric_mass(atmospheric_volume, atmospheric_composition)
            atmospheric_pressure = calculate_atmospheric_pressure(planet_temperature, planet_gravity, atmospheric_mass)
            atmospheric_pressure_hPa = atmospheric_pressure/100000


        else:
            # fill atmospheric data with n/a and 0's
            atmospheric_composition = 'n/a'
            atmospheric_height = 0.0
            atmospheric_volume = 'n/a'
            atmospheric_mass = 'n/a'
            atmospheric_pressure = 0.000
            atmospheric_pressure_hPa = 0.000

        complete_atmospheric_data = {
            'has_atmosphere': has_atmosphere,
            'atmospheric_temperature': temperature,
            'atmospheric_composition': atmospheric_composition,
            'atmosphere_height': atmospheric_height,
            'atmospheric_pressure': atmospheric_pressure,
            'atmospheric_pressure_hPa': atmospheric_pressure_hPa,
        }
        return complete_atmospheric_data


    def ID_generator_planet(self, system_data, planet_data):
        id = system_data['name'] + ' ' + str(planet_data['class_index'] + 1)
        return id

    def ID_generator_star(self, system_data, star_data):
        suffix = self.alphabet[star_data['class_index']]
        id = system_data['name'] + ' ' + suffix
        return id

    def system_name_generator(self, system_seed):
        random.seed(system_seed)
        name = ''
        nr_letters = random.randint(3, 10)
        for i in range(nr_letters):
            rand = random.randint(0, 1)
            if rand:
                name = name + self.vowels[random.randint(0, (len(self.vowels)-1))]
            else:
                name = name + self.consonants[random.randint(0, (len(self.consonants) - 1))]
        name = name.capitalize()
        rand = random.randint(0, 10)
        if rand > 6:
            name = name + ' ' + self.suffix[random.randint(0, (len(self.suffix))-1)]
        return name


