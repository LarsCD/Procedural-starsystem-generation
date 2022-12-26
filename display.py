from GUT import GUT, COLOR
import sys

Fore = COLOR.Fore
Back = COLOR.Back

def display_planet(object):
    planetary_body = object
    atmosphere = planetary_body.atmospheric_data
    composition = []
    if atmosphere['atmospheric_composition'] == 'n/a':
        composition = 'n/a'
    else:
        for i, compound in enumerate(atmosphere['atmospheric_composition'][0]):
            string = f'{Fore.YELLOW()}{compound}{Fore.RESET()} ({round(atmosphere["atmospheric_composition"][1][compound], 3)}%),'
            composition.append(string)

    print('---------------------------------------------------')
    print(f"Type:           {Fore.GREEN()}{planetary_body.type}{Fore.RESET()}")
    print(f"Class:          {Fore.B_BLUE()}{planetary_body.type_name}{Fore.RESET()}")
    print(f"Mass:           {round(planetary_body.mass, 2)} kg")
    print(f"Density:        {round(planetary_body.density, 2)} kg/L")
    print(f'Gravity:        {planetary_body.gravity} m/s')
    print(f'g:              {planetary_body.g} g')
    print(f"Radius:         {planetary_body.radius} km")
    print(f"{Fore.CYAN()}Atmosphere{Fore.RESET()}:")
    print(f'  - {Fore.CYAN()}Has atmosphere{Fore.RESET()}:      {atmosphere["has_atmosphere"]}')
    print(f'  - {Fore.CYAN()}Avg. temperature{Fore.RESET()}:    {atmosphere["atmospheric_temperature"]} K')
    print(f'  - {Fore.CYAN()}Atmosphere height{Fore.RESET()}:   {round(atmosphere["atmosphere_height"])} km')
    print(f'  - {Fore.CYAN()}Surface pressure{Fore.RESET()}: {round(atmosphere["atmospheric_pressure_hPa"], 3)} Bar')
    print(f'  - {Fore.CYAN()}Composition{Fore.RESET()}: ')
    for compound in composition:
        if composition == 'n/a':
            print('         n/a')
            break
        else:
            print(f'    └ {compound}')
    print(f"Has ring:       {planetary_body.has_ring}")
    print(f"Spawn Chance:   {planetary_body.spawn_chance}%")
    print(f"Seed:           ({planetary_body.seed})")
    print(f'[DATA BYTE SIZE]:    [{(sys.getsizeof(planetary_body))} bytes]')