import random
from data import *

weightsType = (77.0, 3.24, 0.36, 15.0, 4.0, 0.4)
usedSeeds = []
stellarObjects = []
seedSizeGlobal = 1000000000



class GenerateStellar:
    def __init__(self, data, seed, spawnChance):
        self.name = data['name']
        self.starClass = data['class']
        self.starType = data['type']
        dataMass = round((random.uniform(data['mass'][0], data['mass'][1])), 2)
        self.mass = dataMass
        self.spawnRate = data['spawnRate']
        self.seed = seed
        self.spawnChance = spawnChance



def generateStellarData(seed):
    # vars
    data = {}
    weightsClass = []

    # set random seed
    random.seed(seed)

    # generate stellar object data (type and class)
    stellarObjType = random.choices(list(stellarObj.keys()), weights=weightsType)

    for i in stellarObj[stellarObjType[0]].values():
        x = i['spawnRate']
        weightsClass.append(x)

    stellarObjClass = random.choices(list((stellarObj[stellarObjType[0]])), weights=weightsClass)

    # get object data
    data = stellarObj[stellarObjType[0]][stellarObjClass[0]]

    # calculate spawn chance
    stellarIndex = list(stellarObj.keys()).index(stellarObjType[0])
    spawnChanceType = weightsType[stellarIndex]
    spawnChanceClass = data['spawnRate']
    spawnChance = round((((spawnChanceType/100)/(1/spawnChanceClass))), 3)

    return data, seed, spawnChance


def generateStellarObjectSet():
    # print('\n'*50)
    setSize = int(input('Set Size: '))
    seedSize = seedSizeGlobal
    rarityThreshhold = float(input('Rarity threshold (100% = all): '))
    duplucatesOption = input('Allow duplicates? (y/n): ')

    print('\nPress [ENTER] to generate stellar objects')
    input()

    print('Generating Stellar Objects...')

    for i in range(setSize):
        seed = random.randint(0, seedSize)
        
        while seed in usedSeeds:
            seed = random.randint(0, seedSize)

        if duplucatesOption == 'n':
            # stores useds seeds to prevent duplicates
            usedSeeds.append(seed)
        
        # creates data for object
        data, seed, spawnChance = generateStellarData(seed)
        
        # creates object
        object = GenerateStellar(data, seed, spawnChance)
        
        # prints data if .spawnChance under rarityThreshhold 
        if object.spawnChance <= rarityThreshhold:
            print(f'''--------------------------------
Stellar Object nr. {i}
{object.name}

Class        : {object.starClass}
Mass         : {object.mass} M☉
Spawn Chance : {object.spawnChance}%
Seed         : {object.seed}
    
--------------------------------''')
    print('\nDONE')
