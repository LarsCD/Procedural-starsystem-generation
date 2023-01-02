from GUT import GUT, COLOR
import sys

Fore = COLOR.Fore
Back = COLOR.Back

class Display:

    def display_planet(object):
        planetary_body = object
        atmosphere = planetary_body.atmospheric_data
        composition = []
        if atmosphere['atmospheric_composition'] == 'n/a':
            composition = 'n/a'
        else:
            for i, compound in enumerate(atmosphere['atmospheric_composition'][0]):
                string = f'{Fore.YELLOW()}{compound}{Fore.RESET()}: {round(atmosphere["atmospheric_composition"][1][compound], 3)}%'
                composition.append(string)

        print('---------------------------------------------------')
        print(f"ID:             {Fore.GREEN()}{planetary_body.id}{Fore.RESET()}")
        print(f"Type:           {Fore.GREEN()}{planetary_body.type}{Fore.RESET()}")
        print(f'Science value:  {Fore.B_BLUE()}{object.science_data}{Fore.RESET()} Σ')
        print(f"Class:          {Fore.B_BLUE()}{planetary_body.type_name}{Fore.RESET()}")
        print(f"Spawn Chance:   {Fore.MAGENTA()}{planetary_body.spawn_chance}%{Fore.RESET()}")
        print('')
        print(f"Mass:           {round(planetary_body.mass, 2)} kg")
        print(f"Density:        {round(planetary_body.density, 2)} kg/L")
        print(f'Gravity:        {planetary_body.gravity} m/s')
        print(f'g:              {planetary_body.g} g')
        print(f"Radius:         {planetary_body.radius} km")
        print(f"Has ring:       {planetary_body.has_ring}")
        print('')
        print(f"{Fore.CYAN()}Atmosphere{Fore.RESET()}:")
        print(f'  - {Fore.CYAN()}Has atmosphere{Fore.RESET()}:      {atmosphere["has_atmosphere"]}')
        print(f'  - {Fore.CYAN()}Avg. temperature{Fore.RESET()}:    {atmosphere["atmospheric_temperature"]} K')
        print(f'  - {Fore.CYAN()}Atmosphere height{Fore.RESET()}:   {round(atmosphere["atmosphere_height"])} km')
        print(f'  - {Fore.CYAN()}Surface pressure{Fore.RESET()}:    {round(atmosphere["atmospheric_pressure_hPa"], 3)} Bar')
        print(f'  - {Fore.CYAN()}Composition{Fore.RESET()}: ')
        for compound in composition:
            if composition == 'n/a':
                print('         n/a')
                break
            else:
                print(f'    └ {compound}')
        print('')
        print(f"Seed:           {planetary_body.seed}")
        print(f'[DATA SIZE]:    {(sys.getsizeof(planetary_body))} bytes')


    def display_star(object):
        print('---------------------------------------------------')
        print(f"ID:             {Fore.GREEN()}{object.id}{Fore.RESET()}")
        print(f'Star:           {Fore.GREEN()}{object.name}{Fore.RESET()}')
        print(f'Science value:  {Fore.B_BLUE()}{object.science_data}{Fore.RESET()} Σ')
        print(f"Type:           {Fore.B_BLUE()}{object.type_name}{Fore.RESET()}")
        print(f"Class:          \'{Fore.B_BLUE()}{object._class[0]}{Fore.RESET()}\'")
        print(f"Spawn Chance:   {Fore.MAGENTA()}{object.spawn_chance}%{Fore.RESET()}")
        print('')
        print(f"Mass:           {round(object.mass_solar, 2)} ☉")
        print(f"Temperature:    {object.temperature} K")
        print('')
        print(f"Seed:           {object.seed}")
        print(f'[DATA SIZE]:    {(sys.getsizeof(object))} bytes')


    def display_system(self, starsystem_data):
        star_count = starsystem_data['star_count']
        planet_count = starsystem_data['planet_count']


