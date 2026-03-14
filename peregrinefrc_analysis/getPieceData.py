

def Robot_died(entry_data: dict) -> bool:
    return "Robot Died" in entry_data["name"]

def Played_defense(entry_data: dict) -> bool:
    return "Played Defense" in entry_data["name"]

def anyFuel(entry_data: dict) -> bool:
    return "Any Fuel Scored" in entry_data["name"]

def tenPlus(entry_data: dict) -> bool:
    return "More Than 10 Fuel Scored" in entry_data["name"]

def fiftyPlus(entry_data: dict) -> bool:
    return "More Than 50 Fuel Scored" in entry_data["name"]

COUNT_FUNCTIONS = [
    anyFuel, 
    tenPlus, 
    fiftyPlus, 
    Played_defense, 
    Robot_died]
COUNT_NAMES = [
    "Any Fuel scored",
    "10 Fuel scored",
    "50 Fuel scored",
    "Played Defense",
    "Robot Died"

]
rankNames = [
    "Before dead bot",
    "After dead bot", ]