stellarObj = {
    'mainSeq': { # 77%
        'O': {'name': 'O Main Sequence Star', 'class': 'O', 'type': 'mainSeq', 'mass': [15, 90], 'spawnRate': 0.2},
        'B': {'name': 'B Main Sequence Star', 'class': 'B', 'type': 'mainSeq', 'mass': [2, 16], 'spawnRate': 1.8},
        'A': {'name': 'A Main Sequence Star', 'class': 'A', 'type': 'mainSeq', 'mass': [1.4, 2.1], 'spawnRate': 6.0},
        'F': {'name': 'F Main Sequence Star', 'class': 'F', 'type': 'mainSeq', 'mass': [1, 1.4], 'spawnRate': 12.0},
        'G': {'name': 'G Main Sequence Star', 'class': 'G', 'type': 'mainSeq', 'mass': [0.8, 1.2], 'spawnRate': 9.0},
        'K': {'name': 'K Main Sequence Star', 'class': 'K', 'type': 'mainSeq', 'mass': [0.6, 0.9], 'spawnRate': 25.0},
        'M': {'name': 'M Main Sequence Star', 'class': 'M', 'type': 'mainSeq', 'mass': [0.4, 0.5], 'spawnRate': 46.0},
    },
    'giant': { # 3.24%
        'B': {'name': 'B Blue-White Supergiant', 'class': 'B', 'type': 'giant', 'mass': [10, 30], 'spawnRate': 1.7},
        'A': {'name': 'A Blue-White Supergiant', 'class': 'A', 'type': 'giant', 'mass': [10, 30], 'spawnRate': 9.2},
        'F': {'name': 'F White Supergiant', 'class': 'F', 'type': 'giant', 'mass': [10, 30], 'spawnRate': 2.1},
        'G': {'name': 'G Yellow Supergiant', 'class': 'G', 'type': 'giant', 'mass': [10, 30], 'spawnRate': 1.6},
        'K': {'name': 'K Orange Giant', 'class': 'K', 'type': 'giant', 'mass': [10, 30], 'spawnRate': 20.0},
        'Mg': {'name': 'M Red Giant', 'class': 'Mg', 'type': 'giant', 'mass': [10, 30], 'spawnRate': 64.0},
        'Ms': {'name': 'M Red Supergiant', 'class': 'Ms', 'type': 'giant', 'mass': [10, 30], 'spawnRate': 1.4},
    },
    'whiteDwarf': { # 0.36%
        'D': {'name': 'White Dwarf', 'class': 'D', 'type': 'whiteDwarf', 'mass': [10, 30], 'spawnRate': 100.0},
    },
    'brownDwarf': { # 15%
        'L': {'name': 'L Brown Dwarf', 'class': 'L', 'type': 'brownDwarf', 'mass': [10, 30], 'spawnRate': 58.0},
        'T': {'name': 'T Brown Dwarf', 'class': 'T', 'type': 'brownDwarf', 'mass': [10, 30], 'spawnRate': 27.0},
        'Y': {'name': 'Y Brown Dwarf', 'class': 'Y', 'type': 'brownDwarf', 'mass': [10, 30], 'spawnRate': 15.0},
    },
    'neutron': { # 4%
        'ns': {'name': 'Neutron Star', 'class': 'n/a', 'type': 'neutron', 'mass': [10, 30], 'spawnRate': 100.0},
    },
    'blackHoles': { # 0.4%
        'bh': {'name': 'Black Hole', 'class': 'n/a', 'type': 'blackHole', 'mass': [10, 1000], 'spawnRate': 98.0},
        'smbh': {'name': 'Supermasive Black Hole', 'class': 'n/a', 'type': 'blackHole', 'mass': [1000, 100000], 'spawnRate': 2.0},
    },
}

planetBody = {
    'mrb': {'name': 'Metal-rich body', 'mass': [0.01, 715.2], 'temp': [45, 47991], 'gravity': 0, 'spawnChance': 1.458},
    'hmcw': {'name': 'High metal concent world', 'mass': [0.01, 1397.9], 'temp': [20, 46100], 'gravity': 0, 'spawnChance': 23.361},
    'rb': {'name': 'Rocky body', 'mass': [0.01, 527.8], 'temp': [20, 51171], 'gravity': 0, 'spawnChance': 16.398},
    'rib': {'name': 'Rocky Ice world', 'mass': [0.01, 298.6], 'temp': [20, 15742], 'gravity': 0, 'spawnChance': 3.541},
    'ib': {'name': 'Icy body', 'mass': [0.01, 2214.0], 'temp': [], 'gravity': 0, 'spawnChance': 43.602},
    'elw': {'name': 'Earth-like world', 'mass': [0.026, 7.1], 'temp': [], 'gravity': 0, 'spawnChance': 0.132},
    'ww': {'name': 'Water world', 'mass': [0.0687, 741.4], 'temp': [], 'gravity': 0, 'spawnChance': 1.571},
    'mrb': {'name': 'Metal-rich body', 'mass': [0.01, 715.2], 'temp': [], 'gravity': 0, 'spawnChance': 1.458},
    'mrb': {'name': 'Metal-rich body', 'mass': [0.01, 715.2], 'temp': [], 'gravity': 0, 'spawnChance': 1.458},
    'mrb': {'name': 'Metal-rich body', 'mass': [0.01, 715.2], 'temp': [], 'gravity': 0, 'spawnChance': 1.458},
    'mrb': {'name': 'Metal-rich body', 'mass': [0.01, 715.2], 'temp': [], 'gravity': 0, 'spawnChance': 1.458},
    'mrb': {'name': 'Metal-rich body', 'mass': [0.01, 715.2], 'temp': [], 'gravity': 0, 'spawnChance': 1.458},
    'mrb': {'name': 'Metal-rich body', 'mass': [0.01, 715.2], 'temp': [], 'gravity': 0, 'spawnChance': 1.458},
    'mrb': {'name': 'Metal-rich body', 'mass': [0.01, 715.2], 'temp': [], 'gravity': 0, 'spawnChance': 1.458},
    'mrb': {'name': 'Metal-rich body', 'mass': [0.01, 715.2], 'temp': [], 'gravity': 0, 'spawnChance': 1.458},
    'mrb': {'name': 'Metal-rich body', 'mass': [0.01, 715.2], 'temp': [], 'gravity': 0, 'spawnChance': 1.458},
    'mrb': {'name': 'Metal-rich body', 'mass': [0.01, 715.2], 'temp': [], 'gravity': 0, 'spawnChance': 1.458},

},


