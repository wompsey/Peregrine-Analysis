
def fuel(entry_data: dict) -> bool:
    return "Fuel" in entry_data["name"]

def l1Auto(entry_data: dict) -> bool:
    return "L1 (auto)" in entry_data["name"]

def l2(entry_data: dict) -> bool:
    return "L2" in entry_data["name"]
def l1(entry_data: dict) -> bool:
    return "L1" in entry_data["name"]
def l3(entry_data: dict) -> bool:
    return "L3" in entry_data["name"]

def Robot_died(entry_data: dict) -> bool:
    return "Robot Died" in entry_data["name"]

def Played_defense(entry_data: dict) -> bool:
    return "Played Defense" in entry_data["name"]




COUNT_FUNCTIONS = [
    fuel,
    l1Auto,
    l1,
    l2,
    l3,
    

]
COUNT_NAMES = [
    "Fuel",
    "L1 (auto)",
    "L1 ",
    "L2 ",
    "L3 ",
    
]

COUNT_SCORE_NAMES = [
    "Fuel Score",
    "l1Auto Score",
    "l1 Score",
    "l2 Score",
    "l3 Score",
    "Auto Score",
    "Teleop Score",
    "Total Score",]

COUNT_STATES_FUNC = [ 
    Played_defense, 
    Robot_died
    ]

COUNT_STATES_NAMES = [
    "Played Defense",
    "Robot Died"
    ]
