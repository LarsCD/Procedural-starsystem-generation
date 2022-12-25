import json

stellar_data = {
    'main_sequence': { # 77%
        'O': {'name': 'O Main Sequence Star', 'class': 'O', 'type': 'main_sequence', 'type_name': 'Main Sequence Star', 'mass': [15, 90], 'spawn_rate': 0.2},
        'B': {'name': 'B Main Sequence Star', 'class': 'B', 'type': 'main_sequence', 'type_name': 'Main Sequence Star', 'mass': [2, 16], 'spawn_rate': 1.8},
        'A': {'name': 'A Main Sequence Star', 'class': 'A', 'type': 'main_sequence', 'type_name': 'Main Sequence Star', 'mass': [1.4, 2.1], 'spawn_rate': 6.0},
        'F': {'name': 'F Main Sequence Star', 'class': 'F', 'type': 'main_sequence', 'type_name': 'Main Sequence Star', 'mass': [1, 1.4], 'spawn_rate': 12.0},
        'G': {'name': 'G Main Sequence Star', 'class': 'G', 'type': 'main_sequence', 'type_name': 'Main Sequence Star', 'mass': [0.8, 1.2], 'spawn_rate': 9.0},
        'K': {'name': 'K Main Sequence Star', 'class': 'K', 'type': 'main_sequence', 'type_name': 'Main Sequence Star', 'mass': [0.6, 0.9], 'spawn_rate': 25.0},
        'M': {'name': 'M Main Sequence Star', 'class': 'M', 'type': 'main_sequence', 'type_name': 'Main Sequence Star', 'mass': [0.4, 0.5], 'spawn_rate': 46.0},
    },
    'giant': { # 3.24%
        'B': {'name': 'B Blue-White Super giant', 'class': 'B', 'type': 'giant', 'type_name': 'Giant', 'mass': [10, 30], 'spawn_rate': 1.7},
        'A': {'name': 'A Blue-White Super giant', 'class': 'A', 'type': 'giant', 'type_name': 'Giant', 'mass': [10, 30], 'spawn_rate': 9.2},
        'F': {'name': 'F White Super giant', 'class': 'F', 'type': 'giant', 'type_name': 'Giant', 'mass': [10, 30], 'spawn_rate': 2.1},
        'G': {'name': 'G Yellow Super giant', 'class': 'G', 'type': 'giant', 'type_name': 'Giant', 'mass': [10, 30], 'spawn_rate': 1.6},
        'K': {'name': 'K Orange Giant', 'class': 'K', 'type': 'giant', 'type_name': 'Giant', 'mass': [10, 30], 'spawn_rate': 20.0},
        'Mg': {'name': 'M Red Giant', 'class': 'Mg', 'type': 'giant', 'type_name': 'Giant', 'mass': [10, 30], 'spawn_rate': 64.0},
        'Ms': {'name': 'M Red Super giant', 'class': 'Ms', 'type': 'giant', 'type_name': 'Giant', 'mass': [10, 30], 'spawn_rate': 1.4},
    },
    'white_dwarf': { # 0.36%
        'D': {'name': 'White Dwarf', 'class': 'D', 'type': 'white_dwarf', 'type_name': 'White Dwarf', 'mass': [10, 30], 'spawn_rate': 100.0},
    },
    'brown_dwarf': { # 15%
        'L': {'name': 'L Brown Dwarf', 'class': 'L', 'type': 'brown_dwarf', 'type_name': 'Brown Giant', 'mass': [10, 30], 'spawn_rate': 58.0},
        'T': {'name': 'T Brown Dwarf', 'class': 'T', 'type': 'brown_dwarf', 'type_name': 'Brown Giant', 'mass': [10, 30], 'spawn_rate': 27.0},
        'Y': {'name': 'Y Brown Dwarf', 'class': 'Y', 'type': 'brown_dwarf', 'type_name': 'Brown Giant', 'mass': [10, 30], 'spawn_rate': 15.0},
    },
    'neutron': { # 4%
        'ns': {'name': 'Neutron Star', 'class': 'n/a', 'type': 'neutron', 'type_name': 'Neutron Star', 'mass': [10, 30], 'spawn_rate': 100.0},
    },
    'black_hole': { # 0.4%
        'bh': {'name': 'Black Hole', 'class': 'n/a', 'type': 'black_hole', 'type_name': 'Black Hole', 'mass': [10, 1000], 'spawn_rate': 98.0},
        'smbh': {'name': 'Supermasive Black Hole', 'class': 'n/a', 'type': 'black_hole', 'type_name': 'Black Hole', 'mass': [1000, 100000], 'spawn_rate': 2.0},
    },
}

with open('data/stellar_data.json', 'w') as file:
    json.dump(stellar_data, file, indent=2)