import random as rand

class Constellation:
    def __init__(self, name, tier, stigma):
        self.name = name
        self.tier = tier
        self.stigma = stigma

# Constellations and their stigmas
def steelLikeDefense():
    pass 
masterOfSteel = Constellation("Master of Steel", "Narrative Grade", steelLikeDefense)

def songOfTheWater():
    pass
navalGeneral = Constellation("Naval General", "Historical Grade", songOfTheWater)

def abyssOfDarkness():
    pass
darkVoidedBird = Constellation("Dark Voided Bird", "Narrative Grade", abyssOfDarkness)

def timeOfVerdict():
    pass
juryOfWater = Constellation("Jury of Water", "Narrative Grade", timeOfVerdict)

def scheming():
    pass
deviousSchemer = Constellation("Devious Schemer", "■■■■■■■", scheming)

def shineBrightLikeADiamond():
    pass
queenOfTheElevenStars = Constellation("Ablazing Sun", "Narrative Grade", shineBrightLikeADiamond)

def lesserBeing():
    pass
duskEffigy = Constellation("Dusk Effigy", "Myth Grade", lesserBeing)

def pinpoint():
    pass
goldenStickAndString = Constellation("Golden Stick and String", "Narrative Grade", pinpoint)

def pewPewPew():
    pass
offenseMaster = Constellation("Offense Master", "Historical Grade", pewPewPew)

def bloodSwipe():
    pass
redBloodManipulator = Constellation("Red Blood Manipulator", "Historical Grade", bloodSwipe)

def grandPitch():
    pass
godOfTheOpera = Constellation("God of The Opera", "Historical Grade", grandPitch)

def crucifix():
    pass
theGrandPriest = Constellation("The Grand Priest", "Historical Grade", crucifix)

def impendingThunder():
    pass
kingOfTheAtmosphericallyChargedChair = Constellation("King of The Atmospherically Charged Chair", "Myth Grade", impendingThunder)

ConstellationList = [masterOfSteel, navalGeneral, darkVoidedBird, juryOfWater, deviousSchemer, queenOfTheElevenStars, duskEffigy, goldenStickAndString, offenseMaster, redBloodManipulator, godOfTheOpera, theGrandPriest, kingOfTheAtmosphericallyChargedChair]
chancesForConstellation = [0.08, 0.1, 0.08, 0.08, 0.001, 0.08, 0.049, 0.08, 0.1, 0.1, 0.1, 0.1, 0.05]

amountOfConstellationsList = [0, 1, 2, 3, 4, 5]
chancesForAmountOfConstellations = [0.25, 0.45, 0.15, 0.075, 0.05, 0.025]



# Chooses Constellation
def randomConstellation():
    global amountOfConstellations
    global chancesForAmountOfConstellations
    global amountOfConstellations
    global ConstellationList
    global chancesForConstellation
    global constellationChoices
    constellationChoices = []
    amountOfConstellations = rand.choices(amountOfConstellationsList, weights = chancesForAmountOfConstellations, k = 1)
    if amountOfConstellations[0] == 0:
        print("No constellations are interested in you.")
    else:
        i = 0
        while (i < amountOfConstellations[0]):
            choice = rand.choices(ConstellationList, weights = chancesForConstellation, k = 1)[0]
        
            if choice in constellationChoices:
                i -= 1
                
            else:
                i += 1
                constellationChoices.append(choice)
                print(choice.name)
 #       make sure its not adding something thats already in the list
 #      if the same object is chosen more than once, it should only be printed once
 #      is it in the list - dont add
 #      is it not in the list - add 
 #      dont print it 
 #      reroll if there is a duplicate
 #      make i minus the amount of times there is a duplicate
        
    
        
    

    
    return ""

randomConstellation()