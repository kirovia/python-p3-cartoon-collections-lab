def roll_call_dwarves(dwarves):
    for dwarf in dwarves:
        print(f'{dwarves.index(dwarf) + 1}. {dwarf}')

def summon_captain_planet(calls):
    return [call.capitalize() + '!' for call in calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(foods):
    cheeses = ['cheddar', 'gouda', 'camembert']
    for cheese in cheeses:
        if cheese in foods:
            return cheese
    return None